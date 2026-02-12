from mcp.server.fastmcp import FastMCP
import tools

mcp = FastMCP("AI Research Assistant")

@mcp.tool()
def summarize_text(text: str) -> str:
    return tools.summarize_text(text)

@mcp.tool()
def extract_key_points(text: str) -> list:
    return tools.extract_key_points(text)

@mcp.tool()
def save_note(note: str) -> str:
    return tools.save_note(note)

@mcp.tool()
def get_notes() -> list:
    return tools.get_notes()

if __name__ == "__main__":
    mcp.run()
