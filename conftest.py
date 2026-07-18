import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT", 30000))  # Default timeout is 30 seconds if not set