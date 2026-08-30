from utils.logger import get_logger

logger = get_logger(__name__)


class AuthAPI:

    def __init__(self, api_client):
        self.api_client = api_client

    def login(self,payload):
        logger.info("Starting Login API")
        response = self.api_client.post(
            "/api/auth/session", data=payload
        )
        logger.info(f"Login API Status Code : %s", response.status)
        return response

    def get_user_info(self, token):

        logger.info("Starting Get User Info API")
        headers = {"Authorization": f"Bearer {token}"}
        response = self.api_client.get("/auth/me", headers=headers)
        logger.info(f"Get User Info API Status Code : %s", response.status)
        return response
