"""Run the Java pmd static code analysis"""

import subprocess
import argparse
from typing import Optional, Sequence
import sys
import os
import collections

# Ref: https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/trailing_whitespace_fixer.py
_PREFIX = "python/starter-python3-project/"
_cmd_to_run = collections.deque(["pytest"])


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_code = 0
    file_prefix = _PREFIX.strip()
    if file_prefix:
        os.chdir(file_prefix)

    for filename in args.filenames:
        if file_prefix:
            filename = filename[len(file_prefix) :]
        print(filename)
        # Any extra checks
        if _skip_file(filename):
            continue
        _cmd_to_run.append(filename)
        with subprocess.Popen(_cmd_to_run) as process:
            try:
                _outs, _errs = process.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                process.kill()
                _outs, _errs = process.communicate()
            return_code += process.returncode
        _cmd_to_run.pop()
    return return_code


def _skip_file(filename: str) -> bool:
    """Boolean logic to skip the current file.

    If no extra skips are needed, simply return `False` and the filename will NOT be skipped.
    """
    return "test/" not in filename and "tests/" not in filename


if __name__ == "__main__":
    sys.exit(main())
