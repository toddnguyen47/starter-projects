#!/bin/bash

set -euxo pipefail

# Must set `_HTML_FILEPATH`` and `_PATH_TO_JACOCOCLI_JAR` as env variables
# using `source`
# You can obtain the latest JAR here: https://github.com/jacoco/jacoco

rm -rf "${_HTML_FILEPATH}"

java \
    -jar "${_PATH_TO_JACOCOCLI_JAR}" \
    report target/jacoco.exec \
    --classfiles target/classes \
    --sourcefiles src/main/java \
    --html "${_HTML_FILEPATH}"
