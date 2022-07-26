#!/bin/bash

set -euxo pipefail
tmpDir="tmp"

mkdir -p "${tmpDir}"
go test -v -coverprofile cover.out ./...
go tool cover -html=cover.out
