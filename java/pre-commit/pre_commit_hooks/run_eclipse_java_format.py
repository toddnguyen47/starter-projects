"""Run `Eclispe formatter` commands in pre_commit_hooks"""

from typing import Optional, Sequence, List
import sys
import argparse
import subprocess
import os.path
import collections

_ECLIPSE_EXE = ""
_FORMATTER_CONFIG = ""


def execute_formatter(list_of_files: List[str]) -> int:
    """Execute `Eclipse formatter` command. Note that this command needs Java 11+"""
    cmd = collections.deque(
        [
            _ECLIPSE_EXE,
            "-nosplash",
            "-data",
            "/tmp/eclipse-workspace",
            "-application",
            "org.eclipse.jdt.core.JavaCodeFormatter",
            "-config",
            _FORMATTER_CONFIG,
        ]
    )
    return_code = 0

    for input_file in list_of_files:
        abs_path = os.path.abspath(input_file)
        cmd.append(abs_path)

        result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
        str_to_write = result.stdout.decode("utf-8").strip()
        print(str_to_write)
        return_code = max(return_code, result.returncode)

        cmd.pop()

    return return_code


def main(_argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", help="list of files")
    args = parser.parse_args()

    return execute_formatter(args.files)


if __name__ == "__main__":
    sys.exit(main())
