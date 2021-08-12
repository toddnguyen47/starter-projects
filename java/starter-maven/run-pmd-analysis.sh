#!/bin/bash

set -eu -o pipefail

_pmd_analysis_dir="pmd-analysis"
_prefix="java/starter-maven"

echo hi > output.log
printf "$@\n" >> output.log

for vararg in "$@"; do
  # Ref: https://stackoverflow.com/a/16623897/6323360
  # Need to delete the prefix
  _cur_file="${vararg#${_prefix}}"
  echo "${_cur_file}" >> output.log
  pmd -d "${_cur_file}"\
    -cache "${_pmd_analysis_dir}/pmd-cache.bin" \
    -rulesets "${_pmd_analysis_dir}/pmd-ruleset.xml"
done

exit 4
