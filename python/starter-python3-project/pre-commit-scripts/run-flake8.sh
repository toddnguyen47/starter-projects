#!/bin/bash

#!/bin/bash

set -e -o pipefail

_prefix="python/starter-python3-project/"

for vararg in "$@"; do
  # Ref: https://stackoverflow.com/a/16623897/6323360
  # Need to delete the prefix
  _cur_file="${vararg#${_prefix}}"
  flake8 "${_cur_file}"
done
