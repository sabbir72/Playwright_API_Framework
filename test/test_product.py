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

# ================================================================

# ================================================================

@allure.feature("Products")
@allure.story("Get All Products")
def test_get_all_products(api_client):

    product_api = ProductAPI(api_client)

    with allure.step("Get all products"):

        response = product_api.get_all_products(limit=5, skip=0)

    print("Status Code:", response.status)

    body = response.json()

    print("All Products Response:", body)

    with allure.step("Validate status code"):

        assert response.status == 200

        allure.attach(
            str(body["products"]),
            name="Products List",
            attachment_type=allure.attachment_type.TEXT
        )
    # with allure.step("Validate response body is a list"):
        
    #     assert isinstance(body, list)

    with allure.step("Validate each product has required fields"):
        assert "products" in body
        allure.attach(
            str(body["products"]),
            name="Products List",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Validate skip field"):
        assert "total" in body

        allure.attach(
            str(body["total"]),
            name="Total Products",
            attachment_type=allure.attachment_type.TEXT

        )
        assert "skip" in body

        allure.attach(
            str(body["skip"]),
            name="Skip Value",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Validate limit field"):
        assert "limit" in body
    with allure.step("Validate products field is a list"):
        assert isinstance(body["products"], list)

    with allure.step("Validate number of products returned"):

        assert len(body["products"]) <= 5

    with allure.step("Validate total"):
        assert body["total"] > 0


# ================================================================

# ================================================================

@allure.feature("Products")
@allure.story("Search Product")

def test_search_product(api_client):

    product_api = ProductAPI(api_client)

    search_query="laptop"

    with allure.step("\n Search for products with query 'laptop'"):

        response = product_api.search_product("laptop")

    print("Status Code:", response.status)

    body = response.json()

    print("\n" + "=" * 50)
    print("SEARCH PRODUCTS RESPONSE")
    print("=" * 50)

    print(f"\nSearch Products Response : {body}")

    print(f"\nStatus Code              : {response.status}")

    print(f"\nSearch Query             : {search_query}")

    print(f"\nTotal Results            : {body['total']}")

    print(f"\nProducts                 : {body['products']}")

    print("=" * 50)

    with allure.step("\n Validate status code"):

        assert response.status == 200

    with allure.step("\n Validate Products Field"):

        assert "products" in body

    with allure.step("\n Validate Total Field"):

        assert "total" in body

    with allure.step("\n Validate Search Results"):

        assert len(body["products"]) > 0



    with allure.step(" \n Validate search results contain products"):

        assert "products" in body

        allure.attach(
            str(body["products"]),
            name="Search Results",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("\n Validate each product has required fields"):

        for product in body["products"]:
            assert "id" in product
            assert "title" in product
            assert "price" in product
            assert "category" in product

            print(
                 f"Product ID: {product["id"]} | "
                 f"Title : {product["title"]}"

            )