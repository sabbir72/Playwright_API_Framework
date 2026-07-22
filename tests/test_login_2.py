import json
from urllib import response
from venv import logger

from api.api_client import APIClient
from api.auth_api import AuthAPI
from utils.json_reader import read_json


def test_login_successful():
    # Step 1: Create an instance of APIClient and AuthAPI
    client = APIClient()

    auth = AuthAPI(client)

    # Step 2: Prepare the login payload

    payload = read_json("payloads/login_payload.json")

    response=auth.login(payload)

    logger.info("=" * 50)
    logger.info("Status Code: %s", response.status)
    logger.info("Response Body: \n%s", response.json())
    logger.info("=" * 50)

    logger.info("=" * 60)

    data = response.json()
    # logger.info("Parsed Response Data: \n%s", json.dumps(data, indent=4))
    assert response.status == 200
    assert data["username"] == "emilys"
    assert "accessToken" in data
    assert "refreshToken" in data
    assert data["accessToken"] != ""
    assert data["refreshToken"] != ""
    logger.info("=" * 60)


    access_token = data.get("access_token")
    logger.info("Access Token: %s", access_token)

    assert access_token != "", "Access token should not be an empty string"

    # print("Response Body: ", response.json())

    # print("Status Code: ", response.status)

    assert response.status == 200

    auth.client.close()
