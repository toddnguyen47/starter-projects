#!/bin/bash

set -eu -o pipefail

_full_path="$HOME/programming/personal/starter-projects/java/pre-commit"
_cur_path="$(pwd)"
pushd "${_full_path}"

# Need an if statement so the command does not exit our script
if python3 "pre_commit_hooks/run_pmd.py" "${_cur_path}/$1"; then
  echo "Success!"
else
  echo "Result: $?"
fi

_python_path="$HOME/programming/personal/pre-commit-hooks"
export PYTHONPATH="${_python_path}"
python3 "${_python_path}/pre_commit_hooks/convert_text_to_html.py" \
  --textfiles "pmd-analysis/output-main.txt, pmd-analysis/output-test.txt" \
  --margin 10
# open "pmd-analysis/output-main.html"
# open "pmd-analysis/output-test.html"
export PYTHONPATH=""

popd
