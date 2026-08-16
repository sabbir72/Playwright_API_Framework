


import json

import allure
from api.auth_api import AuthAPI


@allure.feature("Authentication")
@allure.story("Current user information")
def test_get_current_user(api_client, auth_token):
    auth_api = AuthAPI(api_client)


    with allure.step("Send request to get current user information"):
        response = auth_api.get_user_info(auth_token)

        print("\n" + "=" * 50)
        print("GET CURRENT USER RESPONSE")
        print("=" * 50)
        print(f"\nStatus Code: {response.status}")
        print(f"\nResponse: {json.dumps(response.json(), indent=4)}")
        print("auth_token:", auth_token)

    with allure.step("Verify response status code"):
        assert response.status == 200

    body = response.json()
    with allure.step("Validate username"):
        assert "username" in body
        assert isinstance(body["username"], str)
        assert len(body["username"]) > 0

    with allure.step("Validate user ID"):
        assert "id" in body
        assert isinstance(body["id"], int)
        assert body["id"] > 0

    # print section

    print("\n" + "=" * 50)
    print("GET CURRENT USER RESPONSE")
    print("=" * 50)

    print(f"\nStatus Code   : {response.status}")
    print(f"\nUsername      : {body['username']}")
    print(f"\nUser ID       : {body['id']}")

    print("\n" + "=" * 50)