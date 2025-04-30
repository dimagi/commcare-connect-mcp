# Experimental MCP Server for CommCare Connect (ccc)

This is an experimental MCP server for CommCare Connect.

To use it with [claude code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) you can run `claude` in this folder.
You can see the `.mcp.json` for how it is set up.
 If you want to use a different tool you can modify the declaration accordingly.
 You will need to have `uv` installed on your system, and you may have to specify
 absolute paths to the `uv` executable and `server.py` file.


This project is built on top of the [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk).
