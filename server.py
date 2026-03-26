from mcp.server.fastmcp import FastMCP
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


mcp = FastMCP("my mcp groq server")


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@mcp.tool()
def groq_handle(prompt: str) -> str:
    """Return a Groq LLM response"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    mcp.run()