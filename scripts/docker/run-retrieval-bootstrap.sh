#!/bin/sh

# Named volumes are created as root. Make them writable by the application user
# before running the Python bootstrap with normal application privileges.
set -eu

mkdir -p /app/run /models
chown -R app:app /app/run /models
exec runuser -u app -- python scripts/bootstrap_retrieval_artifacts.py "$@"
