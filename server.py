from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("my mcp groq server")

# Tool function
@mcp.tool()
def greet(name: str) -> str:
    """Return a greeting message"""
    return f"Hello {name} 👋"

# Run server
if __name__ == "__main__":
    mcp.run()