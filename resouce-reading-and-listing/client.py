import asyncio
from fastmcp import Client
from rich import print
import json

async def main():

    # Connect to the running SSE server
    client = Client("http://localhost:8000/sse")

    async with client:
        # resources/list - List all available resources
        resources = await client.list_resources()
        print("Available Resources:")
        for resource in resources:
            print(f"  - {resource.name}: {resource.uri}")
        print("****************************************************************************")


        print("\n All Resouces:", resources)
        print("****************************************************************************")

        config_resource = await client.read_resource("docs://configuration")
        print(f"\nConfiguration Resource:\n{config_resource}")
        print("****************************************************************************")

        payment_resource = await client.read_resource("docs://payment")
        print(f"\nPayment Resource:\n{payment_resource}")
        print("****************************************************************************")

        techmart_products = await client.read_resource("docs://products/techmart")
        print(f"\nTechMart Products:\n{techmart_products}")
        print("****************************************************************************")

        megamart_products = await client.read_resource("docs://products/megamart")
        print(f"\nMegaMart Products:\n{megamart_products}")
        print("****************************************************************************")

        megamart_products = await client.read_resource("docs://products/megamart")
        data = json.loads(megamart_products[0].text)

        print("\n[bold green]MegaMart Products[/bold green]")
        print(json.dumps(data, indent=4))
        print("*" * 80)

        print(f"\nStore: {data['shop']}")

        # Print categories and products in a structured format
        print("\nCategories:")
        for category in data["categories"]:
            print(f"  • {category['name']} ({category['id']})")

        # Print products with details in a readable format
        print("\nProducts:")
        for product in data["products"]:
            print(f"""
        ID        : {product['id']}
        Name      : {product['name']}
        Category  : {product['category']}
        Price     : ${product['price']}
        Discount  : {product['discount']}%
        In Stock  : {product['in_stock']}
        {'-' * 40}
        """)

if __name__ == "__main__":
    asyncio.run(main())