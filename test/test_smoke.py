


def  Test_get_products(api_client):
    response = api_client.get("/products")
    assert response.status == 200
    data = response.json()
    assert isinstance(data, list)
   
    
