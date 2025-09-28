#!/usr/bin/env bash
# Build and upload to TestPyPI. Use environment variables TWINE_USERNAME and TWINE_PASSWORD.
# Example:
#   export TWINE_USERNAME='__token__'
#   export TWINE_PASSWORD='pypi-AgENd...'
#   ./scripts/publish_to_testpypi.sh

set -euo pipefail
cd "$(dirname "$0")/.."
. .venv/bin/activate.fish || true
python -m pip install --upgrade build twine
python -m build --sdist --wheel --outdir dist
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
