import pytest
import requests


class APIClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        print(self.base_address + path)
        return requests.get(url=self.base_address + path, params=params)

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)


@pytest.fixture(scope="session")
def api_brewery():
    return APIClient(base_address="https://api.openbrewerydb.org")
