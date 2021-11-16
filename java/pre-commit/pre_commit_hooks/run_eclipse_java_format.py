"""Run `Eclispe formatter` commands in pre_commit_hooks"""

from typing import Optional, Sequence, List, Set
import sys
import argparse
import subprocess
import os.path

_ECLIPSE_EXE = ""
_FORMATTER_CONFIG = ""

_CMD = [
    _ECLIPSE_EXE,
    "-nosplash",
    "-data",
    "/tmp/eclipse-workspace",
    "-application",
    "org.eclipse.jdt.core.JavaCodeFormatter",
    "-config",
    _FORMATTER_CONFIG,
]


def _parse_ignored_files(ignored_files: str) -> Set[str]:
    """Parse ignored files and return a set of files to ignore"""
    comma_list = ignored_files.split(",")
    result_set = set()
    for file_name in comma_list:
        file_name = file_name.strip()
        result_set.add(file_name)
    return result_set


def _is_file_ignored(input_file: str, ignored_files_set: Set[str]) -> bool:
    """Check if any string in the `ignored_files_set` is a substring of the input_file"""
    for file_name in ignored_files_set:
        if file_name in input_file:
            return True
    return False


def execute_formatter(list_of_files: List[str], ignored_files: str) -> int:
    """Execute `Eclipse formatter` command. Note that this command needs Java 11+"""
    return_code = 0
    ignored_set = _parse_ignored_files(ignored_files)

    list_of_abs_path_files = []
    for input_file in list_of_files:
        if input_file.endswith(".java"):
            if not _is_file_ignored(input_file, ignored_set):
                abs_path = os.path.abspath(input_file)
                list_of_abs_path_files.append(abs_path)

    cmd = _CMD + list_of_abs_path_files
    result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    str_to_write = result.stdout.decode("utf-8").strip()
    print(str_to_write)
    return_code = max(return_code, result.returncode)

    return return_code


def main(_argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    parser.add_argument(
        "--ignore-files", help="Comma-separated list of files to ignore"
    )
    args = parser.parse_args()

    return execute_formatter(args.filenames, args.ignore_files)


if __name__ == "__main__":
    sys.exit(main())

