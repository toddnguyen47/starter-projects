import src.app

import pytest


@pytest.fixture(scope="class")
def app():
    app_obj = src.app.App()
    yield app_obj


class TestApp:
    def test_given_two_when_getting_two_then_should_be_two(self, app: src.app):
        assert 2 == app.return_two()
