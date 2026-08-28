import allure

from api.product_api import ProductAPI

@allure.feature("Products")
@allure.story("Search Products - No Result")
def test_search_product_no_result(api_client):

    product_api = ProductAPI(api_client)

    search_query = "xyznonexistentproduct999"

    with allure.step(f"Search unavailable product: {search_query}"):

        response = product_api.search_products(search_query)

    body = response.json()

    print("Status Code:", response.status)
    print("Search Query:", search_query)
    print("Total Results:", body["total"])

    with allure.step("Validate Status Code"):

        assert response.status == 200

    with allure.step("Validate Products Field"):

        assert "products" in body

    with allure.step("Validate No Search Results"):

        assert body["total"] == 0

    with allure.step("Validate Products List Empty"):

        assert body["products"] == []
