#!/bin/bash

set -euxo pipefail

mvn compile --define "jacoco.skip=true" --define doxygen.skip=true

