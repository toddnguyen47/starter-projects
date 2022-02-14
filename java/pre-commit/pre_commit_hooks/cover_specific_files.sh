#!/bin/bash

set -euxo pipefail

mvn test --define "doxygen.skip=true" \
    --define "test=EventActivationServiceImplTest, EventUtilTest"
pre_commit_hooks/generate_jacoco_report.sh
