#!/bin/bash

mkdir -p .venv
/home/zxatt/.pyenv/shims/python3 -m pipenv install --dev --pre
/home/zxatt/.pyenv/shims/python3 -m pipenv install
