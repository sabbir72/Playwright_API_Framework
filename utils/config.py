import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read Base URL
BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT", 30000))
# ReqRes API Key for testing
REQRES_API_KEY = os.getenv("REQRES_API_KEY")


def get_posts_base_url():
    return os.getenv("POSTS_BASE_URL") or os.getenv("BASE_URL_02")
