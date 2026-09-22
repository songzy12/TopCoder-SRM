#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR/webapp"

if [ -x "$ROOT_DIR/.venv/bin/python" ]; then
	PYTHON="$ROOT_DIR/.venv/bin/python"
else
	PYTHON="python3"
fi

exec "$PYTHON" -m flask --app app.py run --port=8000
