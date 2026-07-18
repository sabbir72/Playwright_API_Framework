from api.api_client import APIClient
from utils.logger import logger

import json


# def test_get_todo():

#     client = APIClient()

#     response = client.get("/todos/1")

#     # print part=====================================================

#     # print("Status:", response.status)

#     # print("\n========== API RESPONSE ==========")
#     # print(f"Status Code : {response.status}")
#     # print("Response Body:")
#     # print(json.dumps(response.json(), indent=4))
#     # print("==================================\n")

#     # assert response.status == 200
#     # assert response.json()["id"] == 1
#     # print part=====================================================

#     # logger part=====================================================

#     logger.info("=" * 50)
#     logger.info("========== API TEST ==========")
#     logger.info("GET TODO API")
#     logger.info("Status Code : %s", response.status)

#     logger.info("Response Body:\n%s",  json.dumps(response.json(), indent=4))

#     logger.info("=" * 50)
#     assert response.status==200

def test_api_key_authentication():
    client = APIClient()

    response = client.get("/api/users/")

    # print part=====================================================

    # print("Status:", response.status)

    # print("\n========== API RESPONSE ==========")
    # print(f"Status Code : {response.status}")
    # print("Response Body:")
    # print(json.dumps(response.json(), indent=4))
    # print("==================================\n")

    # assert response.status == 201
    # assert response.json()["title"] == "New Todo"
    # print part=====================================================

    # logger part=====================================================

    logger.info("=" * 50)
    logger.info("========== API TEST ==========")
    logger.info("REQRES API-KEY AUTHENTICATION: GET USER")
    logger.info("Status Code : %s", response.status)

    logger.info("Response Body:\n%s",  json.dumps(response.json(), indent=4))

    logger.info("=" * 50)
    assert response.status == 200

    client.close()
