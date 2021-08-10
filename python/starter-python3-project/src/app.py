"""Default app"""
from src.mymath import mymath


class App:
    """App class"""

    def __init__(self) -> None:
        self._variable_x = 2

    def return_two(self) -> int:
        """Returns the number 2"""
        self._variable_x = mymath.return_two()
        return self._variable_x
