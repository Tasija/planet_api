import pytest
from utils.https_helper import Https
from utils.helpers import load_json_file


@pytest.fixture()
def https_object(base_url):
    https_object = Https(base_url)
    return https_object


@pytest.fixture(scope='session')
def planet_config():
    """
    Get configuration data
    :return: dict with config loaded data
    """
    return load_json_file("planet_resources.json")


@pytest.fixture(scope="session")
def base_url(request):
    """
    Setup base_url flag
    :param request:
    :return: flag base_url value
    """
    return request.config.getoption("--base_url")


def pytest_addoption(parser):
    parser.addoption("--base_url", action='store', default='remote', help='Set base_url for tests execution')
