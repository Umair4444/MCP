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