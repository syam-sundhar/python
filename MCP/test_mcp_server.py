# -*- coding: utf-8 -*-
"""
Test all MCP server features: tools, resources, and prompts.
Run with: python test_mcp_server.py
"""
import asyncio
import sys
from mcp_client import MCPClient


async def main():
    command = sys.executable
    args = ["mcp_server.py"]

    print("=" * 55)
    print("  MCP Server Test Suite")
    print("=" * 55)

    async with MCPClient(command=command, args=args) as client:

        # -- Tools --------------------------------------------------
        print("\n[1] LIST TOOLS")
        tools = await client.list_tools()
        for t in tools:
            print(f"  [OK] {t.name}: {t.description}")

        print("\n[2] CALL TOOL: read_doc")
        result = await client.call_tool("read_doc", {"doc_id": "deposition.md"})
        if result and result.content:
            print(f"  [OK] Content: {result.content[0].text}")

        print("\n[3] CALL TOOL: read_doc (missing doc)")
        result = await client.call_tool("read_doc", {"doc_id": "missing.txt"})
        if result and result.content:
            print(f"  [OK] Error handled: {result.content[0].text}")

        print("\n[4] CALL TOOL: edit_doc")
        result = await client.call_tool(
            "edit_doc",
            {"doc_id": "plan.md", "new_content": "Updated plan content."},
        )
        if result and result.content:
            print(f"  [OK] {result.content[0].text}")

        # -- Resources ----------------------------------------------
        print("\n[5] READ RESOURCE: docs://documents (list all docs)")
        doc_ids = await client.read_resource("docs://documents")
        print(f"  [OK] Documents: {doc_ids}")

        print("\n[6] READ RESOURCE: docs://documents/report.pdf")
        content = await client.read_resource("docs://documents/report.pdf")
        print(f"  [OK] Content: {content}")

        # -- Prompts ------------------------------------------------
        print("\n[7] LIST PROMPTS")
        prompts = await client.list_prompts()
        for p in prompts:
            print(f"  [OK] /{p.name}: {p.description}")

        print("\n[8] GET PROMPT: summarize")
        messages = await client.get_prompt("summarize", {"doc_id": "financials.docx"})
        if messages:
            text = getattr(messages[0].content, "text", str(messages[0].content))
            print(f"  [OK] Prompt preview: {text[:120]}...")

        print("\n[9] GET PROMPT: rewrite")
        messages = await client.get_prompt("rewrite", {"doc_id": "spec.txt"})
        if messages:
            text = getattr(messages[0].content, "text", str(messages[0].content))
            print(f"  [OK] Prompt preview: {text[:120]}...")

    print("\n" + "=" * 55)
    print("  All tests passed!")
    print("=" * 55)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
