from fastmcp import FastMCP
import json

mcp = FastMCP("Testing Read Resources")

@mcp.resource("docs://configuration")
def app_info():
    return {
        "name": "FastMCP Application",
        "version": "1.0.0",
        "description": "A FastMCP application.",
    }

@mcp.resource("docs://payment")
def payment_info():
    return {
        "name": "FastMCP Payment Service",
        "version": "1.0.0",
        "description": "An example FastMCP payment service.",
    }

@mcp.resource("docs://products/techmart")
def techmart_products():
        # json data to python dict
    with open("shopping_data/techmark.json", "r") as file:
        return json.load(file)
    
@mcp.resource("docs://products/megamart")
def megamart_products():
    # json data to python dict
    with open("shopping_data/megastore.json", "r") as file:
        return json.load(file)

if __name__ == "__main__":
    # Defaults to STDIO transport
    mcp.run()