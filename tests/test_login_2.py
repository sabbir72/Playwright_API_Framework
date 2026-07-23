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
    logger.info(f"Status Code: {response.status}")
    logger.info(json.dumps(response.json(), indent=4))
    logger.info("=" * 50)

    

    data = response.json()
    



    # print("Response Body: ", response.json())

    # print("Status Code: ", response.status)

    assert response.status == 200

    auth.client.close()
