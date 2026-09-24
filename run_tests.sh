#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG_FILE="${RUN_CONFIG:-$ROOT_DIR/run_tests.conf}"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Config file not found: $CONFIG_FILE" >&2
    echo "Create it with: cp run_tests.conf.example run_tests.conf" >&2
    exit 2
fi

# shellcheck source=/dev/null
source "$CONFIG_FILE"

if [ -z "${SOLUTION:-}" ] || [ -z "${TESTS:-}" ]; then
    echo "SOLUTION and TESTS must be set in $CONFIG_FILE" >&2
    exit 2
fi

if [ -x "$ROOT_DIR/.venv/bin/python" ]; then
    PYTHON="$ROOT_DIR/.venv/bin/python"
else
    PYTHON="python3"
fi

cd "$ROOT_DIR"
exec "$PYTHON" scripts/tools/run_tests.py "$SOLUTION" --tests "$TESTS" ${RUN_FLAGS:-}
