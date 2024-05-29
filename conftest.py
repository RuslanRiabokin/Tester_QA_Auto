import pytest
from modules.api.clients.github import GitHub


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api

# My tests
@pytest.fixture(params=['aa', '', '5a', None])
def invalid_quantity(request):
    yield request.param

@pytest.fixture(params=['text', None, GitHub(), 67])
def name_text(request):
    yield request.param