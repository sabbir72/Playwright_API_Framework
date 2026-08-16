import json

import allure

from api.auth_api import AuthAPI


@allure.feature("Authentication")
@allure.story("Negative Login")
class TestAuthNegative:

    def test_wrong_password(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "emilys", "password": "emilyspas"}

        with allure.step("Send login request with wrong password"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("\n Response:", json.dumps(response.json(), indent=4))

        with allure.step("Validate error status"):

            assert response.status == 400

        with allure.step("Validate error message"):

            body = response.json()

            # print(f"Response Body: {body}")

            assert "message" in body
            assert body["message"] == "Invalid credentials"

    def test_wrong_username(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "wronguser", "password": "emilyspass"}

        with allure.step("Send login request with wrong username"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400

    def test_wrong_username_and_password(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "wronguser", "password": "wrongpassword"}

        with allure.step("Send login request with invalid credentials"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400

    def test_missing_password(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "emilys"}

        with allure.step("Send login request without password"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400

    def test_missing_username(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"password": "emilyspass"}

        with allure.step("Send login request without username"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400

    def test_empty_username(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "", "password": "emilyspass"}

        with allure.step("Send login request with empty username"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400

    def test_empty_password(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "emilys", "password": ""}

        with allure.step("Send login request with empty password"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400

    def test_empty_username_and_password(self, api_client):

        auth_api = AuthAPI(api_client)

        payload = {"username": "", "password": ""}

        with allure.step("Send login request with empty credentials"):

            response = auth_api.login(payload)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status == 400


@allure.feature("Authentication")
@allure.story("Authorization")
class TestAuthorizationNegative:

    def test_invalid_token(self, api_client):

        auth_api = AuthAPI(api_client)

        invalid_token = "invalid-token-12345"

        with allure.step("Send request with invalid token"):

         response = auth_api.get_user_info(invalid_token)

        print("Status Code:", response.status)
        print("Response:", json.dumps(response.json(), indent=4))

        assert response.status in [401, 403]

#     def test_missing_token(self, api_client):

#         auth_api = AuthAPI(api_client)

#         with allure.step("Send request without authorization token"):

#             response = api_client.get("/auth/me")

#         print("Status Code:", response.status)
#         print("Response:", json.dumps(response.json(), indent=4))

#         assert response.status in [401, 403]
