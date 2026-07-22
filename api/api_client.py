from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, TIMEOUT





class APIClient: 
    def __init__(self):
       self.playwright = sync_playwright().start()
       self.request = self.playwright.request.new_context(
           base_url=BASE_URL,
           timeout=TIMEOUT
       )

    def get(self, endpoint):
        return self.request.get(endpoint)
    

    def post(self, endpoint, data):
        return self.request.post(endpoint, data=data)   
    
    def close(self):
        self.request.dispose()
        self.playwright.stop()

