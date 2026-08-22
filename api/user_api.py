from utils.logger import get_logger

logger = get_logger(__name__)


class UserAPI:
    def __init__(self,api_client):

        self.api_client=api_client

    def get_users(self, limit=None, skip=None):

        logger. info ("getting all users")

        params = { }

        if limit is not None:
            params["limit"] = limit

        if skip is not None:
            params["skip"] = skip

        response = self.api_client.get("/users", params=params)

        logger.info(f"Get Users API Status Code : %s", {response.status})

        return response



    def get_user_by_id(self, user_id):
        logger.info(f"Getting user by ID: {user_id}")

        response = self.api_client.get(f"/users/{user_id}")

        logger.info(f"Get User by ID API Status Code : %s", {response.status})

        return response


    def search_user(self, query):
        logger.info(f"Searching user {query}")

        response=self.api_client.get("/users/search", params={"q":query})

        logger.info(f"Search user Status: {response.status}")

        return response





    #==========================================

    def create_user(self, payload):
        logger.info("Creating a new user")

        response = self.api_client.post("/users/add", data=payload)

        logger.info(f"Create User API Status Code : %s", {response.status})

        return response

    def update_user(self,user_id, payload):
        logger.info(f"Updating user with ID: {user_id}")

        response = self.api_client.put(f"/users/{user_id}", data=payload)

        logger.info(f"Update User API Status Code : %s", {response.status})

        return response

    def delete_user(self, user_id):
        logger.info(f"Deleting user with ID: {user_id}")

        response = self.api_client.delete(f"/users/{user_id}")
        

        logger.info(f"Delete User API Status Code : %s", {response.status})
        return response
    