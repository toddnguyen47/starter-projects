#!/bin/bash

# Run from folder outside of `pre_commit_hooks`

set -euxo pipefail

# mvn test --define "doxygen.skip=true" --batch-mode
mvn test --define "doxygen.skip=true"
pre_commit_hooks/generate_jacoco_report.sh
