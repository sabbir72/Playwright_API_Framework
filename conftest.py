
import json

import pytest

from api.api_client import APIClient
from api.auth_api import AuthAPI

@pytest.fixture
def api_client():
    client = APIClient()
    yield client
    client.close()

@pytest.fixture
def auth_token(api_client):
    auth_api = AuthAPI(api_client)

    # Load test credentials from JSON file
    with open("payloads/login_payload.json", "r", encoding="utf-8") as file:
        payload = json.load(file)
    
    # Login and get token
    response = auth_api.login(payload)
    assert response.status == 200  # Login must succeed
    body = response.json()
    return body["accessToken"]
   