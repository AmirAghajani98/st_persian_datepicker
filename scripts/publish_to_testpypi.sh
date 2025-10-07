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
# Fail early with a helpful message if twine credentials are missing.
if [ -z "${TWINE_USERNAME:-}" ] || [ -z "${TWINE_PASSWORD:-}" ]; then
	cat <<'MSG'
Error: TWINE_USERNAME and/or TWINE_PASSWORD are not set.

Create an API token on https://test.pypi.org/ (Account -> API tokens) and set the
environment variables before running this script. Example (bash):

	export TWINE_USERNAME='__token__'
	export TWINE_PASSWORD='pypi-AgENd...'

Example (fish shell):

	set -x TWINE_USERNAME '__token__'
	set -x TWINE_PASSWORD 'pypi-AgENd...'

Alternatively use a configured ~/.pypirc file or the keyring backend for twine.
MSG
	exit 1
fi
python -m build --sdist --wheel --outdir dist
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
