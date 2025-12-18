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

USER_PERMISSIONS = {
    "001": "理事",
    "002": "教員",
    "003": "学生"
}

# ユーザー権限を取得するリソース
@mcp.resource("auth://{user_id}/permissions")
def get_user_permissions(user_id: str) -> str:
    """
    指定されたユーザーIDの権限情報を取得します。
    AIはこのURIを介して、ユーザーのアクセスレベルを確認できます。
    """
    permission = USER_PERMISSIONS.get(user_id, "未知のユーザー - 権限情報が見つかりません")
    return f"ユーザーID: {user_id}\n権限ランク: {permission}"

if __name__ == "__main__":
    mcp.run(transport="stdio")