# def main():
#     print("Hello from MCP-Server!")


# if __name__ == "__main__":
#     main()

# MCP Server

# from mcp.server.fastmcp import FastMCP

# mcp = FastMCP("custom-server")

# @mcp.tool()
# def hello():
#     print("Hello from MCP-Server!")

# # @mcp.tool()
# # def add(a: int, b: int) -> int:
# #     return a + b

# # @mcp.tool()
# # def reverse(text: str) -> str:
# #     return text[::-1]

# if __name__ == "__main__":
#     mcp.run()


from fastmcp import FastMCP

mcp = FastMCP("custom-server")

@mcp.tool()
def hello():
    return ("Hello from MCP-Server!")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def reverse(text: str) -> str:
    return text[::-1]

if __name__ == "__main__":
    mcp.run()