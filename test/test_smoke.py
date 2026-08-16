


import json
from urllib import response


def  Test_get_product(api_client):
    response = api_client.get("/products/1")

    print("\n" + "=" * 50)
    print("GET PRODUCT RESPONSE")
    print("=" * 50)

    print(f"\nStatus Code: {response.status}")
    print(f"\nResponse: {json.dumps(response.json(), indent=4)}")

    assert response.status == 200


    body = response.json()


    assert body["id"] == 1
    assert "title" in body
    assert "description" in body
    assert "price" in body



    
    
 