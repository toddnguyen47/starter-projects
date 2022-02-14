"""Test for `app.py`"""

import pytest

from mymath import main


@pytest.fixture(scope="class")
def _init_main():
    """Return a fixture that initializes the App() object"""
    main_obj = main.Main()
    yield main_obj


def test_given_two_when_getting_two_then_should_be_two(_init_main: main):
    """Should return two"""
    assert _init_main.return_two() == 2


def test_given_three_when_getting_two_then_should_not_be_two(_init_main: main):
    """Should not return three"""
    assert _init_main.return_two() != 3
