



import json

from api.api_client import APIClient
from api.auth_api import AuthAPI
from utils.logger import logger
from utils.json_reader import read_json


def test_login_with_valid_credentials():

  #step-1: Create an instance of APIClient and AuthAPI
    client = APIClient()

    #step-2: Create an instance of AuthAPI
    auth = AuthAPI(client)

    #step-3: Read the login payload from the JSON file

    payload = read_json("payloads/login.json")

    #step-4: Call the login method with valid credentials and log the response
    logger.info("=" * 50)
    logger.info("Testing login with valid credentials")

    #step-5: Call the login method with valid credentials and log the response

    response = auth.login(payload)

    body=response.json()
    

    #step-6: Log the status code and response body

    logger.info("Status Code: %s", response.status)
    logger.info("Response Body: \n%s",  json.dumps(body, indent=4)) 

    #step-7: print response body to console
    print("Response Body: ", json.dumps(body, indent=4))
    print("Status Code: ", response.status)


    #step-8: Assert the status code and response body
    assert response.status == 200   
    assert "token" in body
    assert body["token"] != ""


    #step-9: Close the APIClient session
    client.close()
    
