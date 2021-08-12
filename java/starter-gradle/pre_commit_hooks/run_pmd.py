"""Run the Java pmd static code analysis"""

import subprocess
import argparse
from typing import Optional, Sequence

# Ref: https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/trailing_whitespace_fixer.py
_PMD_ANALYSIS_FOLDER = "java/starter-gradle/pmd-analysis"

_pmd_cmd = [
    "pmd",
    "-cache",
    '"' + _PMD_ANALYSIS_FOLDER + '/pmd-cache.bin"',
    "-rulesets",
    '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset.xml"',
    "-dir"
]


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        _pmd_cmd.append(filename)
        with subprocess.Popen(_pmd_cmd) as process:
            try:
                _outs, _errs = process.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                process.kill()
                _outs, _errs = process.communicate()
            return_code += process.returncode
    return return_code


if __name__ == "__main__":
    exit(main())
