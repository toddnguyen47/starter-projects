"""Run `maven` commands in pre_commit_hooks"""

from typing import Optional, Sequence
import sys
import argparse
import subprocess


def execute_maven(args: argparse.Namespace) -> int:
    """Execute `mvn` command

    # Ref: https://stackoverflow.com/a/4760517/6323360
    """
    cmd = ["mvn", args.goal] + args.flags
    print(" ".join(cmd))
    return_code = 0
    result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)

    str_to_write = result.stdout.decode("utf-8").strip()
    print(str_to_write)
    return_code = max(return_code, result.returncode)

    return return_code


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run our checks"""
    parser = argparse.ArgumentParser()
    parser.add_argument("goal", help="maven goals to run")
    parser.add_argument(
        "flags", nargs=argparse.REMAINDER, help="additional flags to pass into maven"
    )
    args = parser.parse_args(argv)

    if not any(args.goal):
        parser.error("No goals provided.")
        return 1

    return execute_maven(args)


if __name__ == "__main__":
    sys.exit(main())
