# def main():
#     print("Hello from MCP-Client!")


# if __name__ == "__main__":
#     main()

import asyncio
from fastmcp import Client
from rich import print

async def main():
    # Connect to your server.py
    client = Client("http://127.0.0.1:8000/sse")

    async with client:
        # Call tools
        result1 = await client.call_tool("hello", {})
        result2 = await client.call_tool("add", {"a": 5, "b": 10})
        result3 = await client.call_tool("reverse", {"text": "mcp"})

        tools = await client.list_tools()
        print("Available tools:", tools)

        print(result1)
        print(result2)
        print(result3)

if __name__ == "__main__":
    asyncio.run(main())