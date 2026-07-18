from utils.config import get_posts_base_url


class PostsAPI:
    """Post resource operations for an API client."""

    def __init__(self, client, endpoint="/posts", base_url=None):
        self.client = client
        self.base_url = base_url or get_posts_base_url()
        self.endpoint = endpoint.rstrip("/") or "/posts"

    def _build_url(self, suffix=""):
        if not self.base_url:
            return self.endpoint + suffix

        base = self.base_url.rstrip("/")
        path = f"{self.endpoint}{suffix}".rstrip("/")
        return f"{base}/{path.lstrip('/')}"

    def get_posts(self):
        return self.client.get(self._build_url())

    def get_post(self, post_id):
        return self.client.get(self._build_url(f"/{post_id}"))

    def create_post(self, payload):
        return self.client.post(self._build_url(), payload)

    def update_post(self, post_id, payload):
        return self.client.put(self._build_url(f"/{post_id}"), payload)

    def patch_post(self, post_id, payload):
        return self.client.patch(self._build_url(f"/{post_id}"), payload)

    def delete_post(self, post_id):
        return self.client.delete(self._build_url(f"/{post_id}"))
