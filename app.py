from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

async def main():

    server = StdioServerParameters(
        command="python",
        args=["server.py"] 
    )

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "greet",
                {"name": "jeevan"}
            )

            print("Result:", result.content[0].text)

asyncio.run(main())