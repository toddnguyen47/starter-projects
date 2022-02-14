#!/bin/bash

set -euo pipefail

# export PYTHONPATH="$(pwd)"
black mymath
pylint mymath
pytest mymath
python3 -m mymath.main
# export PYTHONPATH=""
