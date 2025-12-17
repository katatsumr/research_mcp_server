from fastmcp import FastMCP
import asyncio

# サーバーに名前を付ける
mcp = FastMCP(name="卒論用MCPサーバー")

print("FastMCPサーバーオブジェクトが作成されました。")

# テストのツール
@mcp.tool()
def greet(name: str) -> str:
    """シンプルな挨拶を返します。"""
    return f"こんにちは、{name}さん！"