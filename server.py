from mcp.server.fastmcp import FastMCP

mcp =FastMCP("my mcp grq server")

@mcp.tool()
def greet(name:str)->str:
    return f"this is {name}"

if __name__ == "__main__":
    mcp.run()
