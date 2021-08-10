"""Test for `app.py`"""

import pytest

from src import app


@pytest.fixture(scope="class")
def _init_app():
    """Return a fixture that initializes the App() object"""
    app_obj = app.App()
    yield app_obj


def test_given_two_when_getting_two_then_should_be_two(_init_app: app):
    """Should return two"""
    assert _init_app.return_two() == 2
