import os
import re
import json
from html import unescape
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MAPPING_FILE = os.path.join(ROOT_DIR, 'data', 'problem_mapping.json')
METADATA_FILE = os.path.join(ROOT_DIR, 'data', 'metadata.json')
ARCHIVE_DIR = os.path.join(ROOT_DIR, 'data', 'archive')
ASSET_DIR = os.path.join(os.path.dirname(__file__), '_next')
statistics_cache = None


def build_mapping():
    """Builds a mapping from problem name to its local HTML archive path, if not exists."""
    if os.path.exists(MAPPING_FILE):
        return

    print("Building problem mapping, this might take a few seconds...")
    mapping = {}
    class_pattern = re.compile(
        r'<dt>Class:</dt>\s*<dd>\s*<span>\s*(.*?)\s*</span>\s*</dd>')
    fallback_pattern = re.compile(
        r'<h2>Problem Statement for\s*&quot;(?:<!-- -->)?(.*?)(?:<!-- -->)?&quot;</h2>'
    )

    for root, _, files in os.walk(ARCHIVE_DIR):
        for f in files:
            if f.endswith('.html') and f != 'tc.html':
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()

                        match = class_pattern.search(content)
                        if not match:
                            match = fallback_pattern.search(content)

                        if match:
                            prob_name = match.group(1).strip()
                            # Use forward slashes for URLs
                            # Path stored in mapping needs to be relative to the webapp for URLs or we can just replace ARCHIVE_DIR part
                            rel_filepath = os.path.relpath(
                                filepath,
                                os.path.join(os.path.dirname(__file__), '..'))
                            mapping[prob_name] = rel_filepath.replace('\\', '/')
                except Exception:
                    pass

    with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2)
    print(f"Mapped {len(mapping)} problems.")


def load_data():
    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    return metadata, mapping


def build_statistics(metadata):
    """Extract per-problem statistics from the archived round overview pages."""
    statistics = {}
    difficulty_levels = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
    }

    for year, srms in metadata.items():
        overview_dir = os.path.join(ARCHIVE_DIR, year, 'RoundOverview', 'rd')
        if not os.path.isdir(overview_dir):
            continue

        srm_names = {
            srm_name: {
                problem['problem_name']
                for div in divs
                for problem in div['problems']
            } for srm_name, divs in srms.items()
        }

        for filename in os.listdir(overview_dir):
            if not filename.endswith('.html'):
                continue

            filepath = os.path.join(overview_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
            except OSError:
                continue

            page_stats = {}
            stats_pattern = re.compile(
                r'Division\s+(I{1,2}|\d+)\s+Problem Stats.*?'
                r'<tbody>(.*?)</tbody>', re.IGNORECASE | re.DOTALL)
            row_pattern = re.compile(
                r'<tr>.*?Level\s+(One|Two|Three|Four).*?'
                r'<a[^>]*>\s*([^<]+?)\s*</a>.*?'
                r'<td[^>]*>\s*([\d,]+)\s*</td>.*?'
                r'<td[^>]*>\s*([\d.]+).*?</td>.*?'
                r'<td[^>]*>\s*([\d.]+)\s*</td>.*?</tr>',
                re.IGNORECASE | re.DOTALL)
            for division, table_body in stats_pattern.findall(content):
                division = {'I': '1', 'II': '2'}.get(division, division)
                rows = []
                for level_name, problem_name, submissions, correct_percent, average_points in row_pattern.findall(
                        table_body):
                    level = difficulty_levels[level_name.lower()]
                    rows.append((level, unescape(problem_name.strip()),
                                 submissions.replace(',', ''), correct_percent,
                                 average_points))
                if rows:
                    page_stats[division] = rows

            page_problem_names = {
                problem_name for rows in page_stats.values()
                for _, problem_name, *_ in rows
            }
            matching_srm = max(
                srm_names,
                key=lambda name: len(page_problem_names & srm_names[name]),
                default=None,
            )
            if not matching_srm:
                continue

            match_count = len(page_problem_names & srm_names[matching_srm])
            if match_count < 2:
                continue

            srm_statistics = statistics.setdefault(year, {}).setdefault(
                matching_srm, {})
            for division, rows in page_stats.items():
                division_statistics = srm_statistics.setdefault(division, {})
                for level, problem_name, submissions, correct_percent, average_points in rows:
                    division_statistics[problem_name] = {
                        'level': level,
                        'submissions': submissions,
                        'correct_percent': correct_percent,
                        'average_points': average_points,
                    }

    return statistics


@app.route('/')
def index():
    global statistics_cache
    metadata, mapping = load_data()
    if statistics_cache is None:
        statistics_cache = build_statistics(metadata)
    # Sort years descending
    years = sorted(metadata.keys(), reverse=True)
    return render_template('index.html',
                           metadata=metadata,
                           mapping=mapping,
                           statistics=statistics_cache,
                           years=years)


@app.route('/archive/<path:filename>')
def serve_archive(filename):
    return send_from_directory(ARCHIVE_DIR, filename)


@app.route('/_next/<path:filename>')
def serve_topcoder_asset(filename):
    return send_from_directory(ASSET_DIR, filename)

if __name__ == '__main__':
    build_mapping()
    app.run(debug=True, port=8000)
