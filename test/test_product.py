import allure

from api.product_api import ProductAPI


@allure.feature("Products")
@allure.story("Get Single Product")
def test_get_product(api_client):

    product_api = ProductAPI(api_client)

    with allure.step("Get product by ID"):

        response = product_api.get_product(1)

    print("Status Code:", response.status)

    body = response.json()

    print("Product Response:", body)

    with allure.step("Validate status code"):

        assert response.status == 200

    with allure.step("Validate product ID"):

        assert body["id"] == 1

    with allure.step("Validate product title"):

        assert "title" in body

    with allure.step("Validate product price"):

        assert "price" in body

    with allure.step("Validate product category"):

        assert "category" in body
