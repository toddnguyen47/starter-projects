"""Run the Java pmd static code analysis"""

import subprocess
import argparse
from typing import Optional, Sequence
import sys
import collections

# Ref: https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/trailing_whitespace_fixer.py
_cmd_to_run = collections.deque(["black", "--line-length=120"])


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
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


if __name__ == "__main__":
    sys.exit(main())
