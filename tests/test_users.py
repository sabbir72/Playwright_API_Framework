import json

from api.api_client import APIClient
from utils.json_reader import read_json
from utils.logger import logger


def test_create_user():
    client = APIClient()
    payload = read_json("payloads/create_user.json")

    try:
        response = client.post("/api/users", payload)


        logger.info("=" * 50)
        logger.info("CREATE USER API")
        logger.info("Status Code: %s", response.status)
        logger.info("Response Body: \n%s",  json.dumps(response.json(), indent=4))

        assert response.status == 201
        assert response.json()["name"] == payload["name"]
        assert response.json()["job"] == payload["job"]
        assert "id" in response.json()
    finally:
        client.close()


def test_update_user():
    client = APIClient()
    payload = {"name": "Morpheus", "job": "zion resident"}

    try:
        response = client.put("/api/users/2", payload)

        logger.info("UPDATE USER API")
        logger.info("Status Code: %s", response.status)

        assert response.status == 200
        assert response.json()["job"] == payload["job"]
    finally:
        client.close()


def test_patch_user():
    client = APIClient()
    payload = {"job": "leader"}

    try:
        response = client.patch("/api/users/2", payload)

        logger.info("PATCH USER API")
        logger.info("Status Code: %s", response.status)

        assert response.status == 200
        assert response.json()["job"] == payload["job"]
    finally:
        client.close()


def test_delete_user():
    client = APIClient()

    try:
        response = client.delete("/api/users/2")

        logger.info("DELETE USER API")
        logger.info("Status Code: %s", response.status)

        assert response.status == 204
    finally:
        client.close()
