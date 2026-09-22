#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR/crawler"

echo "Running crawler.py..."
python crawler.py

echo "Running parse_archive.py..."
python parse_archive.py

echo "Crawler scripts finished successfully."
