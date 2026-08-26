import logging

logger = logging.getLogger(__name__)


class ProductAPI:

    def __init__(self, api_client):
        self.api_client = api_client

    def get_product(self, product_id):

        logger.info(f"Getting product with ID: {product_id}")

        response = self.api_client.get(f"/products/{product_id}")

        logger.info(f"Get Product API Status Code: {response.status}")

        return response


    def get_all_products(self, limit=None, skip=None):

        params = {}

        if limit is not None:
            params["limit"] = limit

        if skip is not None:
            params["offset"] = skip

        logger.info(f"Getting all products with params: {params}")

        response = self.api_client.get("/products", params=params)

        logger.info(f"Get All Products API Status Code: {response.status}")

        return response




    def search_product(self, query):
        logger.info(f"Searching for products with query: {query}")

        response = self.api_client.get("/products/search", params={"q": query})

        logger.info(f"Search Product API Status Code: {response.status}")

        return response