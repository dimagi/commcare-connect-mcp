# server.py
import os
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("CommCare Connect MCP")

# Get server endpoint and API key from environment variables
server_endpoint = os.getenv("SERVER_ENDPOINT")
api_key = os.getenv("API_KEY")

if not server_endpoint:
    print("Warning: SERVER_ENDPOINT environment variable not set. Using default value.")
    server_endpoint = "https://ccc.dimagi.com"
if not api_key:
    raise ValueError("API_KEY environment variable not set.")

@mcp.tool()
def get_ccc_server() -> str:
    """Get the CommCare Connect server endpoint"""
    return server_endpoint

@mcp.tool()
def get_api_key() -> str:
    """Get the API key"""
    return api_key

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
