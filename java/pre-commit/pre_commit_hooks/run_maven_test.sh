#!/usr/bin/env sh

set -euxo pipefail

# mvn test --batch-mode --define "jacoco.skip=true" --define doxygen.skip=true
mvn test --define "jacoco.skip=true" --define doxygen.skip=true
# mvn test --batch-mode --define doxygen.skip=true

