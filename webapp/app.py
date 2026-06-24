import os
import re
import json
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

MAPPING_FILE = os.path.join(os.path.dirname(__file__), 'problem_mapping.json')
METADATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'metadata.json')
ARCHIVE_DIR = os.path.join(os.path.dirname(__file__), '..', 'archive')

def build_mapping():
    """Builds a mapping from problem name to its local HTML archive path, if not exists."""
    if os.path.exists(MAPPING_FILE):
        return

    print("Building problem mapping, this might take a few seconds...")
    mapping = {}
    class_pattern = re.compile(r'<dt>Class:</dt>\s*<dd>\s*<span>\s*(.*?)\s*</span>\s*</dd>')
    fallback_pattern = re.compile(r'<h2>Problem Statement for\s*&quot;(?:<!-- -->)?(.*?)(?:<!-- -->)?&quot;</h2>')

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
                            rel_filepath = os.path.relpath(filepath, os.path.join(os.path.dirname(__file__), '..'))
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

@app.route('/')
def index():
    metadata, mapping = load_data()
    # Sort years descending
    years = sorted(metadata.keys(), reverse=True)
    return render_template('index.html', metadata=metadata, mapping=mapping, years=years)

@app.route('/archive/<path:filename>')
def serve_archive(filename):
    return send_from_directory(ARCHIVE_DIR, filename)

if __name__ == '__main__':
    build_mapping()
    app.run(debug=True, port=8000)
