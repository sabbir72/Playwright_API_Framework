from playwright.sync_api import sync_playwright
from utils.config import API_TIMEOUT, BASE_URL
from utils.logger import get_logger


logger = get_logger(__name__)

class APIClient:
    def __init__(self):
        self.playwright = sync_playwright().start()

        self.request=self.playwright.request.new_context(
            base_url=BASE_URL,
            timeout=API_TIMEOUT
        )

        logger.info("API Client initialized")

    def get(self, endpoint, **kwargs):

        logger.info(f"GET Request: {endpoint}")

        response = self.request.get(endpoint, **kwargs)

        logger.info(f"GET Response: {response.status}")

        return response

    def post(self, endpoint, **kwargs):

        logger.info(f"POST Request: {endpoint}")

        response = self.request.post(endpoint, **kwargs)

        logger.info(f"POST Response: {response.status}")

        return response

    def put(self, endpoint, **kwargs):

        logger.info(f"PUT Request: {endpoint}")

        response = self.request.put(endpoint, **kwargs)

        logger.info(f"PUT Response: {response.status}")

        return response

    def delete(self, endpoint, **kwargs):

        logger.info(f"DELETE Request: {endpoint}")

        response = self.request.delete(endpoint, **kwargs)

        logger.info(f"DELETE Response: {response.status}")

        return response

    def close(self):

        logger.info("Closing API Client")

        self.request.dispose()
        self.playwright.stop()
