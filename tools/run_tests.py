#!/usr/bin/env python3
"""Run JSON example cases against a TopCoder-style Python class."""

import argparse
import importlib.util
import json
import sys
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
