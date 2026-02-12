import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


def detect_intent(user_input: str):
    user_input = user_input.lower()

    if "summarize" in user_input:
        return "summarize_text"

    if "extract key points" in user_input or "key points" in user_input:
        return "extract_key_points"

    if "save this note" in user_input or "save note" in user_input:
        return "save_note"

    if "show my saved notes" in user_input or "show notes" in user_input:
        return "get_notes"

    return None


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server/server.py"],
    )

    async with stdio_client(server_params) as (read_stream, write_stream):

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            print("Offline MCP Research Assistant 🚀")
            print("Type 'exit' to quit.\n")

            while True:
                user_input = input("You: ")

                if user_input.lower() == "exit":
                    break

                tool_name = detect_intent(user_input)

                if not tool_name:
                    print("Assistant: I can summarize, extract key points, save notes, or show notes.")
                    continue

                # Extract actual content
                content = user_input.split(":", 1)
                argument_text = content[1].strip() if len(content) > 1 else ""

                if tool_name == "get_notes":
                    result = await session.call_tool(tool_name, {})
                elif tool_name == "save_note":
                    result = await session.call_tool(tool_name, {"note": argument_text})
                else:
                    result = await session.call_tool(tool_name, {"text": argument_text})

                # Clean output
                if result.structuredContent:
                    print("Assistant:", result.structuredContent.get("result"))
                elif result.content:
                    print("Assistant:", result.content[0].text)
                else:
                    print("Assistant: No response.")

if __name__ == "__main__":
    asyncio.run(main())
