import pytest
import requests
from datetime import datetime

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def reqres_url():
    return "https://reqres.in"

@pytest.fixture(scope="function")
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

@pytest.fixture(scope="function")
def reqres_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer QpwL5tke4Pnpja7X4"  # This is a dummy token for testing
    }

@pytest.fixture(scope="function")
def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

@pytest.fixture(scope="function")
def session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="function")
def test_data():
    return {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }

@pytest.fixture(scope="function")
def user_data():
    return {
        "name": "Test User",
        "job": "Test Engineer"
    } 