import json
from urllib import response

import allure

from api.auth_api import AuthAPI

@allure.feature("Authentication")
@allure.story("Successful login")
def test_login_success(api_client):
    auth_api = AuthAPI(api_client)

    with open("payloads/login_payload.json","r", encoding="utf-8") as file:
        payload = json.load(file)

    with allure.step("Send login request"):
        response = auth_api.login(payload)

        print("\n" + "=" * 60)
        print("LOGIN RESPONSE")
        print("=" * 60)
    
        print(f"URL         : {response.url}")
        print(f"Status Code : {response.status}")
        print(f"Status Text : {response.status_text}")
    
        print("\nResponse Body:")
        print(response.text())
    
        print("=" * 60)
     
    with allure.step("Verify response status code"):
        assert response.status == 200

    # with allure.step("Verify response status code"):
    #     assert response.status == 200

    # body = response.json()
    # with allure.step("Validate username"):
    #     assert body["username"] == payload["username"]

  

    

    # with allure.step("Validate user ID"):
    #     assert "id" in body
    #     assert body["id"] > 0

    # with allure.step("Validate token"):
    #     assert "accessToken" in body
    #     assert isinstance(body["accessToken"], str)
    #     assert len(body["accessToken"]) > 0

    # with allure.step("Validate refresh token"):
    #     assert "refreshToken" in body
    #     assert isinstance(body["refreshToken"], str)
    #     assert len(body["refreshToken"]) > 0

    # # print section

    # print("\n" + "=" * 50)
    # print("LOGIN RESPONSE")
    # print("=" * 50)

    # print(f"\nStatus Code   : {response.status}")
    # print(f"\nUsername      : {body['username']}")
    # print(f"\nUser ID       : {body['id']}")
    # print(f"\nAccess Token  : {body['accessToken']}")
    # print(f"\nRefresh Token : {body['refreshToken']}")

    # print("\n" + "=" * 50)
