
"""Run the Java pmd static code analysis"""

import subprocess
import argparse
from typing import Optional, Sequence, List
import collections
import os
import time

# Ref: https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/trailing_whitespace_fixer.py
_PREFIX = "java/starter-gradle/"
_PMD_ANALYSIS_FOLDER = "pmd-analysis"
_UTF8_ENCODING = "utf-8"
_CACHE_FILE_EXT = ".bin"
_BASE_CACHE_NAME_MAIN = 'pmd-cache-main' + _CACHE_FILE_EXT
_BASE_CACHE_NAME_TEST = 'pmd-cache-test' + _CACHE_FILE_EXT
_INDEX_CACHE_NAME = 2

_pmd_cmd_main = collections.deque(
    [
        "pmd",
        "-cache",
        '"' + _PMD_ANALYSIS_FOLDER + '/cache/' + _BASE_CACHE_NAME_MAIN + '"',
        "-rulesets",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset-main.xml"',
        "-format",
        "html",
        "-dir",
    ]
)

_pmd_cmd_test = collections.deque(
    [
        "pmd",
        "-cache",
        '"' + _PMD_ANALYSIS_FOLDER + '/cache/' + _BASE_CACHE_NAME_TEST + '"',
        "-rulesets",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset-test.xml"',
        "-format",
        "html",
        "-dir",
    ]
)

_cmds = [_pmd_cmd_main, _pmd_cmd_test]
_output_files = [_PMD_ANALYSIS_FOLDER + "/output-main.html", _PMD_ANALYSIS_FOLDER + "/output-test.html"]


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_code = 0
    _remove_output_files(_output_files)
    file_prefix = _PREFIX.strip()
    if file_prefix:
        os.chdir(file_prefix)
        for index, filename in enumerate(args.filenames):
            args.filenames[index] = filename[len(file_prefix):]

    file_list = ",".join(args.filenames)

    for cmd, output_file in zip(_cmds, _output_files):
        cmd.append("\"{}\"".format(file_list))
        print(" ".join(cmd))
        with subprocess.Popen(cmd, stdout=subprocess.PIPE) as process:
            try:
                stdout, _stderr = process.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, _stderr = process.communicate()
            return_code = max(return_code, process.returncode)
            with open(output_file, "a+") as file:
                str_to_write = stdout.decode(_UTF8_ENCODING).strip()
                if str_to_write:
                    file.write(str_to_write)
        cmd.pop()
    return return_code


def _remove_output_files(filenames: List[str]):
    """Remove output files"""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
            time.sleep(0.5)


if __name__ == "__main__":
    exit(main())
