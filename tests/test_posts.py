from api.posts_api import PostsAPI


class DummyClient:
    def __init__(self):
        self.calls = []

    def get(self, endpoint):
        self.calls.append(("GET", endpoint))
        return endpoint

    def post(self, endpoint, payload):
        self.calls.append(("POST", endpoint, payload))
        return endpoint

    def put(self, endpoint, payload):
        self.calls.append(("PUT", endpoint, payload))
        return endpoint

    def patch(self, endpoint, payload):
        self.calls.append(("PATCH", endpoint, payload))
        return endpoint

    def delete(self, endpoint):
        self.calls.append(("DELETE", endpoint))
        return endpoint


def test_posts_api_uses_env_base_url(monkeypatch):
    monkeypatch.setenv("POSTS_BASE_URL", "https://jsonplaceholder.typicode.com")
    client = DummyClient()
    api = PostsAPI(client)

    assert api.get_posts() == "https://jsonplaceholder.typicode.com/posts"
    assert api.get_post(1) == "https://jsonplaceholder.typicode.com/posts/1"
