# MCP with Agent

This project is a Model Context Protocol (MCP) implementation featuring both a server and a client designed for interactive agent workflows.

## Project Structure

- `server.py`: The MCP server implementation. It provides tools and resources as defined by the Model Context Protocol, serving as the backend for content and logic access.
- `client.py`: The MCP client implementation. It handles connections to the MCP server, sending requests and processing responses to facilitate interaction.
- `agents_client/`: Agent-specific client code and main entry point. This directory contains the logic for higher-level agentic workflows built on top of the base client.
- `data/`: Contains sample data and rules (books.json, rules.json) used by the server to provide context.
- `pyproject.toml`: Project configuration and dependencies (managed by `uv`).

## Architecture

This project follows a standard MCP client-server architecture:
- **Server (`server.py`)**: This is the host for data, tools, and resources. It implements the MCP protocol to expose these assets. **Yes, it is necessary** for the client to work, as the client relies on the server to provide the functional context and data it operates upon.
- **Client (`client.py` / `agents_client/`)**: This acts as the consumer of the server's capabilities. It connects to the server to execute tools, fetch data, or interact with resources.

## Running the Project

Because the client depends on the server's provided context, you must ensure the server is active or properly configured to communicate with the client.

1. **Start the Server**: 
   Depending on your implementation, this usually involves starting the server process so it can listen for incoming connections:
   ```bash
   uv run server.py
   ```

2. **Run the Client**: 
   In a separate terminal (while the server is running), execute the agent client:
   ```bash
   uv run agents_client/main.py
   ```

*Note: Depending on how your MCP implementation is structured (e.g., standard I/O vs. HTTP/SSE), the client may automatically spawn the server process for you. Check your configuration if the client fails to connect.*

## License

MIT
