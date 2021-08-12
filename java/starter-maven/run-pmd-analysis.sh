#!/bin/bash

set -eu -o pipefail

_pmd_analysis_dir="pmd-analysis"
pmd -d src\
  -cache "${_pmd_analysis_dir}/pmd-cache.bin" \
  -rulesets "${_pmd_analysis_dir}/pmd-ruleset.xml"
