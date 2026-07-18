class AuthAPI:
    """Authentication-related ReqRes API operations."""

    def __init__(self, client):
        self.client = client

    def login(self, payload):
        return self.client.post("/api/login", payload)

    def get_authenticated_user(self, user_id=2):
        return self.client.get(f"/api/users/{user_id}")
