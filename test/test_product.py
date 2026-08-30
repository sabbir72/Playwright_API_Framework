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

    with allure.step("\n Search for products with query {search_query}"):

        response = product_api.search_product(search_query)

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
                 f"Title : {product["title"]} | "
                 f"price : {product ["price"]}"

            )

    # =========================================

    # =========================================

    @allure .feature(product)
    @allure.story("Create product")

    def test_create_product(api_client):

        product_api=ProductAPI(api_client)

        payload = {"title": "QA Test Product", "price": 99.99, "category": "beauty"}

        with allure.step("Prepare product payload"):

            print("Create Product Payload:", payload)

            allure.attach(
                str(payload),
                name="Create Product Payload",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Create product"):

            response = product_api.create_product(payload)

        print("Status Code:", response.status)

        body = response.json()

        print("Create Product Response:", body)

        with allure.step("Validate Status Code"):

            assert response.status == 201

        with allure.step("Validate Product ID"):

            assert "id" in body
            assert body["id"] is not None

        with allure.step("Validate Product Title"):

            assert body["title"] == payload["title"]

        with allure.step("Validate Product Price"):

            assert body["price"] == payload["price"]

        with allure.step("Validate Product Category"):

            assert body["category"] == payload["category"]
# =============================================================

# =============================================================

@allure.feature("Products")
@allure.story("Update Product")
def test_update_product(api_client):

    product_api = ProductAPI(api_client)

    product_id = 1

    update_payload = {"title": "Updated QA Product", "price": 149.99}

    with allure.step("Prepare update payload"):

        print("Update Payload:", update_payload)

        allure.attach(
            str(update_payload),
            name="Update Product Payload",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step(f"Update product with ID: {product_id}"):

        response = product_api.update_product(product_id, update_payload)

    print("Status Code:", response.status)

    body = response.json()

    print("Update Response:", body)

    with allure.step("Validate Status Code"):

        assert response.status == 200

    with allure.step("Validate Product ID"):

        assert body["id"] == product_id

    with allure.step("Validate Updated Title"):

        assert body["title"] == update_payload["title"]

    with allure.step("Validate Updated Price"):

        assert body["price"] == update_payload["price"]


# ===========================================
 #delete 
# ===========================================


@allure.feature("Products")
@allure.story("Delete Product")
def test_delete_product(api_client):

    product_api = ProductAPI(api_client)

    product_id = 1

    with allure.step(f"Delete product with ID: {product_id}"):

        response = product_api.delete_product(product_id)

    print("Delete Status Code:", response.status)

    body = response.json()

    print("Delete Response:", body)

    with allure.step("Validate Status Code"):

        assert response.status == 200

    with allure.step("Validate Deleted Product ID"):

        assert body["id"] == product_id

    with allure.step("Validate Deleted Flag"):

        assert body.get("isDeleted") is True

    with allure.step("Validate Deleted Date"):

        assert "deletedOn" in body
