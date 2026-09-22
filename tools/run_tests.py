#!/usr/bin/env python3
"""Run JSON example cases against a TopCoder-style Python class."""

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def load_solution(solution_path):
    module_name = solution_path.stem
    spec = importlib.util.spec_from_file_location(module_name, solution_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load solution: {solution_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solution_class = getattr(module, module_name)
    return solution_class()


def default_test_path(solution_path):
    relative_path = solution_path.relative_to(Path.cwd())
    parts = relative_path.parts
    if len(parts) < 4 or parts[0] != "SRM":
        raise ValueError(
            "Cannot infer tests path. Use --tests for solutions outside SRM/<year>/<round>."
        )
    year, round_name = parts[1:3]
    return Path("tests") / year / round_name / f"{solution_path.stem}.json"


def run(solution_path, test_path):
    with test_path.open(encoding="utf-8") as file:
        test_data = json.load(file)

    if solution_path.suffix == ".cpp":
        return run_cpp(solution_path, test_data)

    solution = load_solution(solution_path)
    method = getattr(solution, test_data["method"])
    failures = 0

    for index, case in enumerate(test_data["cases"], start=1):
        actual = method(*case["args"])
        expected = case["expected"]
        if actual == expected:
            print(f"PASS {index}: {case['args']} -> {actual}")
        else:
            failures += 1
            print(
                f"FAIL {index}: {case['args']} -> expected {expected}, got {actual}"
            )

    total = len(test_data["cases"])
    print(f"\n{total - failures}/{total} cases passed")
    return failures == 0


def cpp_literal(value, type_name):
    type_name = " ".join(type_name.replace("const", "").split())
    if type_name.endswith("&"):
        type_name = type_name[:-1].strip()
    if type_name in {"string", "std::string"}:
        return json.dumps(value)
    if type_name in {"bool"}:
        return "true" if value else "false"
    if type_name in {"double", "float"}:
        return repr(value)
    if type_name.startswith("vector<") or type_name.startswith("std::vector<"):
        element_type = type_name[type_name.find("<") + 1:-1].strip()
        return "{" + ", ".join(
            cpp_literal(item, element_type) for item in value) + "}"
    return str(value).lower() if isinstance(value, bool) else str(value)


def cpp_method_signature(source, method_name):
    pattern = re.compile(
        rf"(?P<return>[A-Za-z_][\w:<>, ]*?)\s+{re.escape(method_name)}\s*"
        rf"\((?P<parameters>[^()]*)\)",
        re.MULTILINE,
    )
    match = pattern.search(source)
    if not match:
        raise ValueError(f"Cannot find C++ method signature for {method_name}")

    parameter_types = []
    parameters = match.group("parameters").strip()
    if parameters:
        for parameter in parameters.split(","):
            parameter = re.sub(r"=\s*.*$", "", parameter).strip()
            parameter = re.sub(r"\b[A-Za-z_]\w*\s*$", "", parameter).strip()
            parameter_types.append(parameter)
    return match.group("return").strip(), parameter_types


def run_cpp(solution_path, test_data):
    source = solution_path.read_text(encoding="utf-8")
    method_name = test_data["method"]
    return_type, parameter_types = cpp_method_signature(source, method_name)
    class_match = re.search(r"\bclass\s+([A-Za-z_]\w*)", source)
    if not class_match:
        raise ValueError("Cannot find C++ solution class")
    class_name = class_match.group(1)

    cases = []
    for case in test_data["cases"]:
        if len(case["args"]) != len(parameter_types):
            raise ValueError(f"Argument count mismatch in case: {case['args']}")
        arguments = ", ".join(
            cpp_literal(value, type_name)
            for value, type_name in zip(case["args"], parameter_types))
        expected = cpp_literal(case["expected"], return_type)
        cases.append((arguments, expected))

    source_literal = json.dumps(str(solution_path))
    test_lines = []
    for index, (arguments, expected) in enumerate(cases, start=1):
        test_lines.append(
            f"    {{ {class_name} solution; auto actual = solution.{method_name}({arguments}); "
            f"auto expected = {expected}; if (actual == expected) {{ ++passed; "
            f"cout << \"PASS {index}\" << endl; }} else {{ ++failed; "
            f"cout << \"FAIL {index}: expected \" << expected << \" got \" << actual << endl; }} }}"
        )

    harness = f'''#include <bits/stdc++.h>
using namespace std;
#define main topcoder_solution_main
#include {source_literal}
#undef main

int main() {{
    int passed = 0, failed = 0;
{chr(10).join(test_lines)}
    cout << passed << "/" << (passed + failed) << " cases passed" << endl;
    return failed == 0 ? 0 : 1;
}}
'''

    with tempfile.TemporaryDirectory(prefix="topcoder-tests-") as temporary:
        temporary_path = Path(temporary)
        harness_path = temporary_path / "main.cpp"
        executable_path = temporary_path / "runner"
        harness_path.write_text(harness, encoding="utf-8")
        compile_result = subprocess.run(
            [
                "g++", "-std=c++17", "-O2",
                str(harness_path), "-o",
                str(executable_path)
            ],
            capture_output=True,
            text=True,
        )
        if compile_result.returncode:
            print(compile_result.stderr, file=sys.stderr)
            return False
        result = subprocess.run([str(executable_path)], text=True)
        return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("solution", type=Path)
    parser.add_argument("--tests", type=Path, help="Override the inferred JSON test path")
    args = parser.parse_args()

    solution_path = args.solution.resolve()
    test_path = (args.tests or default_test_path(solution_path)).resolve()
    if not test_path.exists():
        print(f"Test file not found: {test_path}", file=sys.stderr)
        return 2

    return 0 if run(solution_path, test_path) else 1


if __name__ == "__main__":
    raise SystemExit(main())
