"""Run the Java pmd static code analysis"""

import subprocess
import argparse
from typing import Optional, Sequence, List
import collections
import os

# Ref: https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/trailing_whitespace_fixer.py
_PREFIX = "java/starter-maven/"
_PMD_ANALYSIS_FOLDER = "pmd-analysis"
_UTF8_ENCODING = "utf-8"

_pmd_cmd_main = collections.deque(
    [
        "pmd",
        "-cache",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-cache-main.bin"',
        "-rulesets",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset-main.xml"',
        "-format",
        "text",
        "-dir",
    ]
)

_pmd_cmd_test = collections.deque(
    [
        "pmd",
        "-cache",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-cache-test.bin"',
        "-rulesets",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset-test.xml"',
        "-format",
        "text",
        "-dir",
    ]
)

_cmds = [_pmd_cmd_main, _pmd_cmd_test]
_output_files = [_PMD_ANALYSIS_FOLDER + "/output-main.log", _PMD_ANALYSIS_FOLDER + "/output-test.log"]


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_code = 0
    _remove_output_files(_output_files)
    os.chdir(_PREFIX)
    for cmd, output_file in zip(_cmds, _output_files):
        for filename in args.filenames:
            filename = filename[len(_PREFIX):]
            print(filename)
            cmd.append(filename)
            with subprocess.Popen(cmd, stdout=subprocess.PIPE) as process:
                try:
                    stdout, _stderr = process.communicate(timeout=15)
                except subprocess.TimeoutExpired:
                    process.kill()
                    stdout, _stderr = process.communicate()
                return_code += process.returncode
                with open(output_file, "a+") as file:
                    str_to_write = stdout.decode(_UTF8_ENCODING).strip()
                    if str_to_write:
                        file.write(str_to_write)
                        file.write("\n")
            cmd.pop()
    return return_code


def _remove_output_files(filenames: List[str]):
    """Remove output files"""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == "__main__":
    exit(main())
