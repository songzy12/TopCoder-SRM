#!/bin/bash
cd "$(dirname "$0")"

echo "Running crawler/crawler.py..."
python crawler/crawler.py

echo "Running crawler/parse_archive.py..."
python crawler/parse_archive.py

echo "Crawler scripts finished successfully."
