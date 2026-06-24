#!/bin/bash
cd "$(dirname "$0")/webapp"
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=8000
