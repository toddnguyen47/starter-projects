#!/bin/bash

set -euxo pipefail

mvn clean
rm -rfv target
mvn compile --define "jacoco.skip=true" --define doxygen.skip=true

