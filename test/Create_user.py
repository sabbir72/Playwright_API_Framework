import allure

from api.user_api import UserAPI

@allure.feature("Users")
@allure.story("Create User")

def test_create_user(api_client):
    user_api = UserAPI(api_client)

    payload = {
        "firstName": "Sabbir",
        "lastName": "ahamed",
        "email": "sabbircse72@gmail.com"
        }

    with allure.step("Create a new user"):
        response= user_api.create_user(payload)


        print("Status Code:", response.status)

        body=response.json()

        print("User Created:", body)

        assert response.status == 201


        with allure.step("Verify the created user details"):
            assert body["firstName"] == payload["firstName"]
            assert body["lastName"] == payload["lastName"]
            assert body["email"] == payload["email"]
            assert "id" in body

