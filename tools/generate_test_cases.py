#!/usr/bin/env python3
"""Generate JSON test cases from archived TopCoder problem statements."""

import argparse
import ast
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT_DIR / "archive"
METADATA_FILE = ROOT_DIR / "metadata.json"
DEFAULT_OUTPUT_DIR = ROOT_DIR / "tests"


def split_values(text):
    values = []
    start = 0
    depth = 0
    quote = None
    escaped = False
    for index, character in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote:
                quote = None
        elif character in "\"'":
            quote = character
        elif character in "[{(":
            depth += 1
        elif character in "]})":
            depth -= 1
        elif character == "," and depth == 0:
            values.append(text[start:index].strip())
            start = index + 1
    final_value = text[start:].strip()
    if final_value:
        values.append(final_value)
    return values


def parse_value(text):
    text = text.strip()
    if text.startswith("{") and text.endswith("}"):
        inner = text[1:-1].strip()
        return [] if not inner else [parse_value(value) for value in split_values(inner)]
    if text.startswith('"') and text.endswith('"'):
        return json.loads(text)
    if text.startswith("'") and text.endswith("'"):
        return ast.literal_eval(text)
    if text.lower() == "true":
        return True
    if text.lower() == "false":
        return False
    if re.fullmatch(r"[-+]?\d+", text):
        return int(text)
    if re.fullmatch(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?", text):
        return float(text)
    raise ValueError(f"unsupported value: {text!r}")


def statement_details(path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    class_element = soup.find("dt", string=lambda value: value and value.strip() == "Class:")
    method_element = soup.find("dt", string=lambda value: value and value.strip() == "Method:")
    examples_heading = next(
        (heading for heading in soup.find_all(["h2", "h3"])
         if heading.get_text(" ", strip=True).lower() == "examples"),
        None,
    )
    if not class_element or not method_element or not examples_heading:
        raise ValueError("missing class, method, or examples section")

    class_name = class_element.find_next("dd").get_text(" ", strip=True)
    method_name = method_element.find_next("dd").get_text(" ", strip=True)
    examples = []
    ordered_list = examples_heading.find_next("ol")
    if not ordered_list:
        raise ValueError("missing examples list")

    for item in ordered_list.find_all("li", recursive=False):
        paragraphs = [element.get_text(" ", strip=True)
                      for element in item.find_all(["p", "pre"])]
        return_index = next(
            (index for index, value in enumerate(paragraphs)
             if value.startswith("Returns:")),
            None,
        )
        if return_index is None:
            continue
        argument_values = [parse_value(value) for value in paragraphs[:return_index]]
        expected = parse_value(paragraphs[return_index][len("Returns:"):].strip())
        examples.append({"args": argument_values, "expected": expected})

    if not examples:
        raise ValueError("no parseable examples")
    return class_name, method_name, examples


def build_statement_index():
    index = {}
    class_pattern = re.compile(
        r'<dt>Class:</dt>\s*<dd>\s*<span>\s*(.*?)\s*</span>\s*</dd>',
        re.DOTALL,
    )
    for path in ARCHIVE_DIR.glob("*/ProblemStatement/pm/*.html"):
        year = path.parts[-4]
        match = class_pattern.search(path.read_text(encoding="utf-8"))
        if match:
            index.setdefault((year, match.group(1).strip()), path)
    return index


def generate(output_dir):
    metadata = json.loads(METADATA_FILE.read_text(encoding="utf-8"))
    statement_index = build_statement_index()
    generated = 0
    skipped = []
    skipped_rounds = []

    for year, srms in metadata.items():
        for round_name, divisions in srms.items():
            if not round_name.startswith("SRM "):
                skipped_rounds.append((year, round_name))
                continue
            round_directory = round_name[4:]
            for division in divisions:
                for problem in division["problems"]:
                    name = problem["problem_name"]
                    statement = statement_index.get((year, name))
                    if not statement:
                        skipped.append((year, round_name, name, "statement not found"))
                        continue
                    try:
                        class_name, method_name, cases = statement_details(statement)
                    except (OSError, ValueError, SyntaxError, json.JSONDecodeError) as error:
                        skipped.append((year, round_name, name, str(error)))
                        continue
                    destination = output_dir / year / round_directory / f"{name}.json"
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_text(
                        json.dumps({"method": method_name, "cases": cases}, indent=2) + "\n",
                        encoding="utf-8",
                    )
                    generated += 1

    print(f"Generated {generated} JSON files.")
    print(f"Skipped {len(skipped)} problems.")
    print(f"Skipped {len(skipped_rounds)} non-SRM contests:")
    for year, round_name in skipped_rounds:
        print(f"SKIP CONTEST {year}/{round_name}")
    for year, round_name, name, reason in skipped:
        print(f"SKIP {year}/{round_name}/{name}: {reason}")
    return 0 if not skipped else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    return generate(args.output_dir.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
