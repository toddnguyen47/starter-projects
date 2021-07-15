#!/bin/bash

mkdir -p .venv
python3 -m pipenv install --dev --pre
python3 -m pipenv install
