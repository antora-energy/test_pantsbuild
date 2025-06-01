# hack to get httpx into the pex build.  It's needed specifically for testing fastapi

import httpx  # noqa: F401
from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello from Liz!"}
