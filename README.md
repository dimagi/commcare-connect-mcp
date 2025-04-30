# Experimental MCP Server for CommCare Connect (ccc)

This is an experimental MCP server for CommCare Connect.

To use it with [claude code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) you can run `claude` in this folder.
You can see the `.mcp.json` for how it is set up.
If you want to use a different tool you can modify the declaration accordingly.
You will need to have `uv` installed on your system, and you may have to specify
absolute paths to the `uv` executable and `server.py` file.


This project is built on top of the [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk).

## Usage

At the moment all this can do is query the global stats API which is used by the
[program dashboard](https://connect.dimagi.com/admin_reports/program_dashboard).
So basically you can ask it questions about amounts earned and paid, active users,
and visit stats, optionally over specific date ranges (or programs/organizations if you know their IDs).

## Getting an authentication token

The easiest way to get an authentication token is as a superuser to visit
[https://connect.dimagi.com/admin/authtoken/tokenproxy/](https://connect.dimagi.com/admin/authtoken/tokenproxy/)
and find a token associated with your email.

If you don't have any tokens, you can run the following, replacing your username and password:

```
curl -X POST -d "username=you@dimagi.com&<password=***" https://connect.dimagi.com/auth-token/
```

This will create a token and print its value on the command line.

You can test that the token is valid with the following:

curl -H "Authorization: Token YOUR_TOKEN" "https://connect.dimagi.com/admin_reports/api/dashboard_stats/?from_date=2024-01-01&to_date=2024-12-31"


## Development

You can change the `SERVER_ENDPOINT` in `.mcp.json` to http://localhost:8000 to test this against a development server.
This will require running a development server and getting an API token through the same process as above against it.

You can also run it against [https://connect-staging.dimagi.com/](https://connect-staging.dimagi.com/) with a similar process.
