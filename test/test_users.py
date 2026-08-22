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


def test_get_single_user(api_client):

    user_api = UserAPI(api_client)

    user_id = 90

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


def test_get_users_with_skip(api_client):

    user_api = UserAPI(api_client)

    response = user_api.get_users(limit=100, skip=3)

    print("Status Code:", response.status)

    body = response.json()

    print("Skip:", body["skip"])
    print("Limit:", body["limit"])

    assert response.status == 200
    assert body["skip"] == 3
    assert body["limit"] == 100
