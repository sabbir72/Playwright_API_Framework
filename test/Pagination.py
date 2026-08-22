import allure
from api.user_api import UserAPI

@allure.feature("Users")
@allure.story("Pagination")
def test_get_users_with_limit(api_client):

    user_api = UserAPI(api_client)

    response = user_api.get_users(limit=5)

    print("Status Code:", response.status)

    body = response.json()

    print("Users Returned:", len(body["users"]))

    assert response.status == 200
    assert body["limit"] == 5
    assert len(body["users"]) <= 5

# এবার প্রথম 5 বাদ দিয়ে পরের data.
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
