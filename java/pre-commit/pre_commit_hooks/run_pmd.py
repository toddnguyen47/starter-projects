"""Run the Java pmd static code analysis"""

import subprocess
import argparse
from typing import Optional, Sequence, List
import collections
import os
import time
import sys

import dominate
from dominate import tags

# Ref: https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/trailing_whitespace_fixer.py
_PREFIX = "change/path/to/"
_PMD_ANALYSIS_FOLDER = "pmd-analysis"
_UTF8_ENCODING = "utf-8"
_CACHE_FILE_EXT = ".bin"
_BASE_CACHE_NAME_MAIN = "pmd-cache-main" + _CACHE_FILE_EXT
_BASE_CACHE_NAME_TEST = "pmd-cache-test" + _CACHE_FILE_EXT
_INDEX_CACHE_NAME = 2
_OUTPUT_FORMAT = "text"
_OUTOUT_MAIN_FILE = "/output-main.html"
_OUTPUT_TEST_FILE = "/output-test.html"

_pmd_cmd_main = collections.deque(
    [
        "pmd",
        "-cache",
        '"' + _PMD_ANALYSIS_FOLDER + "/cache/" + _BASE_CACHE_NAME_MAIN + '"',
        "-rulesets",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset-main.xml"',
        "-format",
        _OUTPUT_FORMAT,
        "-dir",
    ]
)

_pmd_cmd_test = collections.deque(
    [
        "pmd",
        "-cache",
        '"' + _PMD_ANALYSIS_FOLDER + "/cache/" + _BASE_CACHE_NAME_TEST + '"',
        "-rulesets",
        '"' + _PMD_ANALYSIS_FOLDER + '/pmd-ruleset-test.xml"',
        "-format",
        _OUTPUT_FORMAT,
        "-dir",
    ]
)

_cmds = [_pmd_cmd_main, _pmd_cmd_test]
_output_files = [
    _PMD_ANALYSIS_FOLDER + _OUTOUT_MAIN_FILE,
    _PMD_ANALYSIS_FOLDER + _OUTPUT_TEST_FILE,
]


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
            args.filenames[index] = filename[len(file_prefix) :]

    file_list = ",".join(args.filenames)

    for cmd, output_file in zip(_cmds, _output_files):
        cmd.append(f'"{file_list}"')
        print(" ".join(cmd))
        with subprocess.Popen(cmd, stdout=subprocess.PIPE) as process:
            try:
                stdout, _stderr = process.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, _stderr = process.communicate()
            return_code = max(return_code, process.returncode)
            with open(output_file, "a+", encoding=_UTF8_ENCODING) as file:
                str_to_write = stdout.decode(_UTF8_ENCODING).strip()
                html_text = _generate_html_from_txt(output_file, str_to_write)
                file.write(str(html_text))
        cmd.pop()
    return return_code


def _remove_output_files(filenames: List[str]):
    """Remove output files"""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
            time.sleep(0.5)


def _generate_html_from_txt(doc_title: str, input_str: str) -> str:
    """Generate a simple HTML file from txt file"""
    doc = dominate.document(title=doc_title)

    with doc.head:
        tags.style(
            r"html{font-size:62.5%;}body{font-size:1.8rem;}div.content{width:1024px;margin:auto;}"
            + r"p.pmd-text{font-family:monospace;}"
        )

    with doc:
        with tags.div(_class="content"):
            if input_str.strip():
                for line in input_str.split("\n"):
                    tags.p(line, _class="pmd-text")
            else:
                tags.p("You're good! No errors ✨ 🍰 ✨", _class="pmd-text")

    return doc


if __name__ == "__main__":
    sys.exit(main())
