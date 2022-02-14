"""Default app"""
from logger_color import logger_color
from mymath import mymath


class Main:
    """Main class"""

    def __init__(self) -> None:
        self._variable_x = 2

    def return_two(self) -> int:
        """Returns the number 2"""
        self._variable_x = mymath.return_two()
        return self._variable_x


def _main():
    """Main function to run binary"""
    main = Main()
    logger = logger_color.init_logger(__name__, logger_color.LoggerType.BOTH)
    logger.debug("DEBUG")
    logger.info(f"return_two() returns: ${main.return_two()}")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL, cannot continue")


if __name__ == "__main__":
    _main()
