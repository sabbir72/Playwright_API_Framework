# import allure
# import pytest

# from api.user_api import UserAPI


# @allure.feature("users")
# @allure.story("Delte User with negtive parameterized user IDs")
# @pytest.mark.parametrize("user_id", [-1, 0, 9999, "abc", None])

# def test_delete_invalite_user(api_client,user_id):

#     user_api= UserAPI(api_client)

#     with allure.step(f"Delete user with invalid ID: {user_id}"):
#         response = user_api.delete_user(user_id)

#         print(f"User Id: {user_id}")

#         print(f"Status code: {response.status}")

#         print(f"Response: {response.json()}")

#         assert response.status==404


import pytest
import allure

from api.user_api import UserAPI


@allure.feature("Users")
@allure.story("Delete User - Negative")
@pytest.mark.parametrize(
    "user_id",
    [
        pytest.param(-1, id="negative-id"),
        pytest.param(0, id="zero-id"),
        pytest.param(9999, id="non-existing-id"),
        pytest.param("abc", id="string-id"),
        pytest.param(None, id="null-id"),
    ]
)
def test_delete_invalid_user(api_client, user_id):

    user_api = UserAPI(api_client)

    with allure.step(
        f"Delete user with invalid ID: {user_id}"
    ):

        response = user_api.delete_user(user_id)

    print(f"User ID: {user_id}")
    print(f"Status Code: {response.status}")
    print(f"Response: {response.json()}")

    assert response.status in [400, 404]