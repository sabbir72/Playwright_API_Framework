import allure
from api.user_api import UserAPI
@allure.feature("Users")
@allure.story("Get Single User")
def test_get_single_user(api_client):

    user_api = UserAPI(api_client)

    user_id = 999999

    with allure.step("Get user by ID"):

        response = user_api.get_user_by_id(user_id)

    print("Status Code:", response.status)

    body = response.json()

    print("User:", body)
    print("First Name:", body.get("firstName"))
    print("Last Name:", body.get("lastName"))
    print("Email:", body.get("email"))
    print("ID:", body.get("id"))

    assert response.status == 200

    assert body["id"] == user_id
    assert "firstName" in body
    assert "lastName" in body
    assert "email" in body
