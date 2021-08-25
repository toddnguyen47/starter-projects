"""Default app"""
from mymath import mymath
import logger_color
from logger_color import LoggerType


class App:
    """App class"""

    def __init__(self) -> None:
        self._variable_x = 2

    def return_two(self) -> int:
        """Returns the number 2"""
        self._variable_x = mymath.return_two()
        return self._variable_x


def _main():
    """Main function to run binary"""
    logger = logger_color.init_logger(__name__, LoggerType.BOTH)
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL, cannot continue")


if __name__ == "__main__":
    _main()
