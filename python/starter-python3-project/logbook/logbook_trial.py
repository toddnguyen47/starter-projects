"""Logbook logger trial"""

import sys

import logbook

_LOG_LEVEL = logbook.INFO


def main():
    setup = logbook.NestedSetup(
        [
            logbook.StreamHandler(sys.stdout, level=_LOG_LEVEL, bubble=True),
            logbook.RotatingFileHandler("log.txt", level=_LOG_LEVEL, bubble=True),
        ]
    )
    with logbook.Flags(introspection=False):
        with setup.applicationbound():
            main_helper()


def main_helper():
    log = logbook.Logger("my_log")
    log.info(f"Hello world! Log level: {_LOG_LEVEL}")


if __name__ == "__main__":
    main()
