MCP AI Research Assistant (Offline)

📌 Overview

An offline AI Research Assistant built using the Model Context Protocol (MCP).
The system uses a FastMCP server exposing structured tools and a custom client orchestrator communicating via stdio transport.

This project demonstrates end-to-end MCP integration without external APIs.


🚀 Features:


Summarize research text
Extract key points
Save research notes locally
Retrieve saved notes
Fully offline
stdio-based MCP transport
Structured tool invocation

🏗 Architecture

User CLI

   ↓
   
MCP Client

   ↓ (stdio transport)
   
FastMCP Server

   ↓
   
Tool Execution Layer

   ↓
   
notes.json


🛠 Tech Stack:

Python 3.13
Model Context Protocol (MCP) v1.26.0
FastMCP
AsyncIO

▶️ How To Run:

1. Clone repository
git clone https://github.com/paneri11/mcp-ai-research-assistant.git
cd mcp-ai-research-assistant

2. Create virtual environment:
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run:
python client/client.py
