import allure
import pytest

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


#=========================================

#=========================================



@pytest.mark.parametrize(
    "product_id",
    [-1, 0, 99999, "abc"]
)
@allure.feature("Products")
@allure.story("Delete Product - Negative")
def test_delete_invalid_product(
    api_client,
    product_id
):

    product_api = ProductAPI(api_client)

    with allure.step(
        f"Delete invalid product ID: {product_id}"
    ):

        response = product_api.delete_product(
            product_id
        )

    print(
        f"Product ID: {product_id}"
    )

    print(
        f"Status Code: {response.status}"
    )

    print(
        f"Response: {response.text()}"
    )

    with allure.step("Validate Error Response"):

        assert response.status in [400, 404]