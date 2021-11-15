"""Run `Eclispe formatter` commands in pre_commit_hooks"""

from typing import Optional, Sequence, List
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

def execute_formatter(list_of_files: List[str]) -> int:
    """Execute `Eclipse formatter` command. Note that this command needs Java 11+"""
    return_code = 0

    list_of_abs_path_files = []
    for input_file in list_of_files:
        if input_file.endswith(".java"):
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
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args()

    return execute_formatter(args.filenames)


if __name__ == "__main__":
    sys.exit(main())
