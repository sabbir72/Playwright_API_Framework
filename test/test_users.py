import allure

from api.user_api import UserAPI


@allure.feature("Users")
@allure.story("Get All Users")
def test_get_all_users(api_client):

    user_api = UserAPI(api_client)

    with allure.step("Get all users"):

        response = user_api.get_users()

    print("Status Code:", response.status)

    body = response.json()

    print("Total Users:", body["total"])
    print("Users Returned:", len(body["users"]))

    assert response.status == 200

    assert "users" in body
    assert "total" in body
    assert "skip" in body
    assert "limit" in body

    assert len(body["users"]) > 0
