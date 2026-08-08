import json

from playwright.sync_api import sync_playwright


def  test_smoke():
    with sync_playwright() as p:

        request = p.request.new_context(
            base_url="https://dummyjson.com"
        )

        response = request.get("/products/10")
        assert response.ok
        assert response.status == 200

        print("Response body:")
        print(json.dumps(response.json(), indent=4))
        print("Response status:", response.status)

        request.dispose()

    
