import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read Base URL
BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT", 30000))







# Base url 2=====================================

