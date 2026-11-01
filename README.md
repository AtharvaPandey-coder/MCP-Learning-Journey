# MCP Learning Journey

A hands-on learning journey exploring the **Model Context Protocol (MCP)** using Python. This repository covers MCP fundamentals, server and client development, tool execution, resources, prompts, Groq AI integration, and security practices.

## What I Learned and Implemented

### Day 1 – MCP Fundamentals
- Understanding Model Context Protocol (MCP).
- Understanding MCP Host, Client, Server, and Tools.
- Difference between MCP tools and LangChain tools.

### Day 2 – MCP Server Setup
- Created an MCP server using the Python MCP SDK.
- Implemented calculator tools.
- Connected tools to the MCP server.

### Day 3 – Building an MCP Client
- Connected an MCP client to the server.
- Discovered available tools using `list_tools()`.
- Executed tools using `call_tool()`.
- Tested communication between the client and server.

### Day 4 – Resources and Prompts
- Explored MCP Resources.
- Implemented a calculator information resource.
- Created an MCP prompt using `@mcp.prompt()`.
- Understood how resources and prompts differ from tools.

### Day 5 – Integrating MCP with Groq AI
- Integrated Groq AI with the MCP client.
- Used dynamic tool discovery.
- Converted MCP tool schemas into Groq-compatible tool definitions.
- Implemented AI-driven tool selection and execution.
- Returned tool results to the AI for its final response.

### Day 6 – Security and Error Handling
- Input validation for calculator operations.
- Exception handling during tool execution.
- Safe tool execution using an allowlist.
- Basic prompt injection defence.
- Role-based tool permissions for user, admin, and guest roles.
- Tested valid inputs, invalid inputs, and unauthorized tool access.

## Project Structure

```text
MCP-Learning-Journey/
│
├── server.py
├── client.py
├── ai_app.py
├── requirements.txt
├── README.md
```

## Technologies Used

- Python
- Model Context Protocol (MCP)
- Groq API
- Asyncio

## Setup and Installation

**1. Clone the repository**

```bash
git clone https://github.com/AtharvaPandey-coder/MCP-Learning-Journey
cd MCP-Learning-Journey
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure your Groq API key**

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file or expose your API key.

**4. Run the MCP server client**

```bash
python client.py
```

**5. Run the AI-powered MCP application**

```bash
python ai_app.py
```

## Key Learning Outcome

This journey helped me understand how MCP enables AI applications to discover and use external tools through a standardized protocol.

I also gained practical experience connecting an AI model with an MCP server, executing tools dynamically, handling errors, and implementing basic security controls.

---

*This repository documents Days 1–6 of my MCP learning journey. The final practical project is maintained separately.*
