
from api.api_client import APIClient
from utils.config import BASE_URL






# for base url=====================================

class AuthAPI:
    """Authentication-related ReqRes API operations."""

    def __init__(self, client):
        self.client = client

    def login(self, payload):
        return self.client.post(f"{BASE_URL}/auth/login", payload)  
    