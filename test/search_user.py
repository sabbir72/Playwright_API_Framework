import allure
from api.user_api import UserAPI

@allure.feature("Users")
@allure.story("Search User")
def test_search_user(api_client):

    user_api = UserAPI(api_client)

    with allure.step("Search user by query"):

        response = user_api.search_user("Isabella")

    print("Status Code:", response.status)

    body = response.json()

    print("Search Results:", body)
    print("Search Results user ID:", body.get("id"))

    assert response.status == 200

    assert "users" in body
    assert "total" in body
