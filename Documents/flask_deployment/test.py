import pytest

from main import app

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_pages(client):
    index = client.get("/")
    assert index.status_code == 200
    test = client.get("/test")
    assert test.status_code == 200
    numbers = client.get("/123")
    assert numbers.status_code == 200
