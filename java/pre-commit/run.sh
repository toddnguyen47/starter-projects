#!/bin/bash

set -euxo pipefail

_full_path="/Users/programming/personal/starter-projects/java/pre-commit"

pushd "${_full_path}"
python3 "pre_commit_hooks/run_pmd.py" "$*"
popd
