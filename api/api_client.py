

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

        