from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, REQRES_API_KEY, TIMEOUT


class APIClient:

    def __init__(self):
        self.playwright = sync_playwright().start()

        self.request = self.playwright.request.new_context(
            base_url=BASE_URL,
            timeout=TIMEOUT,
        )

    @staticmethod
    def _default_headers():
        headers = {"X-Reqres-Env": "prod"}
        if REQRES_API_KEY:
            headers["x-api-key"] = REQRES_API_KEY
        return headers

    def get(self, endpoint):
        return self.request.get(endpoint, headers=self._default_headers())

    def post(self, endpoint, data):
        return self.request.post(
            endpoint,
            data=data,
            headers=self._default_headers(),
        )

    def put(self, endpoint, data):
        return self.request.put(
            endpoint,
            data=data,
            headers=self._default_headers(),
        )

    def patch(self, endpoint, data):
        return self.request.patch(
            endpoint,
            data=data,
            headers=self._default_headers(),
        )

    def delete(self, endpoint):
        return self.request.delete(endpoint, headers=self._default_headers())

    def close(self):
        self.request.dispose()
        self.playwright.stop()
