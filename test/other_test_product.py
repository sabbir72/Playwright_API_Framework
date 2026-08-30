import allure
from api.product_api import ProductAPI

from utils.schema_validator import validate_schema

@allure.feature("Product other test")
@allure.story("product response validation")


def test_product_validation(api_client):
    product_api=ProductAPI(api_client)

    product_id=1

    with allure.step(f"Get with product ID:{product_id}"):

        response= product_api.get_product(product_id)

        body=response.json()

        print("\n ========= product response validation =======")

        print(f"Status code: {response.status}")

        with allure.step("Validation status code"):
            assert response.status==200

        with allure.step("validate schema"):
            schema_path = ("schemas/product_schema.json")

            validate_schema(
                body, schema_path
            )

            print(f"\n Product schema validation pass")

        with allure.step("validate required product"):
            required_field =[
               "id",
               "title",
               "price",
               "category",
               "stock"
           ]

            for field in required_field:
                assert field in body,(
               f"Required field missing :{field}"
            )

                print(f"\n Required field exists: {field}")

    #  data type check ===================================

    with allure.step("validate product data type"):

        assert isinstance (body["id"], int)

        assert isinstance (body["title"], str)

        assert isinstance(body["price"], (int,float))

        print(f"\n Data types are valid")

    # test buiness values ===================================================

    with allure.step("validate product buisness values"):

        assert body["id"]==product_id

        assert body["price"] >= 0

        assert body["stock"]>= 0

        assert body["title"].strip() !=""

        assert body["category"].strip() !=""

        print("Buisnee values are valid")

    with allure.step("validate dimensions"):
        assert "dimensions" in body

        dimensions= body["dimensions"]

        assert "width" in dimensions
        assert "height" in dimensions
        assert "depth" in dimensions

        print("validate dimensions")

    with allure.step(" validate reviews "):

        assert "reviews" in body

        reviews=body["reviews"]

        assert isinstance(reviews, list)

        for review in reviews:
            assert "rating" in review
            assert "comment" in review
            assert "reviewerName" in review
            assert "reviewerEmail" in review

        print(f"Reviews validation :{len(reviews)}")
