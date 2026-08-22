from urllib import response

import allure

from api.user_api import UserAPI

@allure.feature("Users")
@allure.story("Delete User")

def test_delete_user(api_client):
    user_api= UserAPI(api_client)

    user_id= 11

    with allure.step("Delete existing user"):
        response= user_api.delete_user(user_id)
    print("Delete Status Code:", response.status)



    body=response.json()
    print("Delete Response:", body)


    with allure.step("Validate status code"):
        assert response.status== 200


    with allure.step("Validate deleted user ID"):
        assert body["id"]== user_id

    with allure.step("validate seleted status:"):
        assert body["isDeleted"] is True

    with allure.step("validate delteted timestamp"):
        assert "deletedOn" in body