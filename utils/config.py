

import os

from dotenv import load_dotenv
 
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30000"))
