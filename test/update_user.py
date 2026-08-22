import allure

from api.user_api import UserAPI


@allure.feature("Users")
@allure.story("Update User")
def test_update_user(api_client):

    user_api = UserAPI(api_client)

    user_id = 1

    payload = {"firstName": "SabbirUpdated", "lastName": "AhamedUpdated", "age": 30}

    with allure.step("Update existing user"):

        response = user_api.update_user(user_id, payload)

    print("Status Code:", response.status)

    body = response.json()

    print("Update Response:", body)

    with allure.step("Validate status code"):

        assert response.status == 200

    with allure.step("Validate user ID"):

        assert body["id"] == user_id

    with allure.step("Validate updated first name"):

        assert body["firstName"] == "SabbirUpdated"

    with allure.step("Validate updated last name"):

        assert body["lastName"] == "AhamedUpdated"

    with allure.step("Validate updated age"):

        assert body["age"] == 30
