import allure

from api.user_api import UserAPI

@allure.feature("User")
@allure.story("Get al user")

def test_get_all_user(api_client):

    user_api=UserAPI(api_client)

    user_id=1

    with allure.step("Get all users"):
        response=user_api.get_users(user_id)

        print("Status code:", response.status)

        body=response.json()

        print("Total users:", body["total"])
        print("Users Returned:", len(body["users"]))

        assert response.status == 200

        assert "users" in body
        assert "total" in body
        assert "skip" in body
        assert "limit" in body

        assert len(body["users"]) > 0





