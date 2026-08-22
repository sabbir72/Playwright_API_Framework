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
