from fastmcp import FastMCP
import pandas as pd
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


# csvデータを読み込み、JSONに変換するデータ
def csv_to_json(path):
    df = pd.read_csv(path)
    json_data = df.to_json(force_ascii=False)
    return df, json_data


data_1 = "設問1データ.csv"
data_2 = "設問2データ.csv"
data_3 = "設問3データ.csv"
data_4 = "設問4データ.csv"
data_5 = "設問5データ.csv"

df_1, user_input_1 = csv_to_json(data_1)
df_2, user_input_2 = csv_to_json(data_2)
df_3, user_input_3 = csv_to_json(data_3)
df_4, user_input_4 = csv_to_json(data_4)
df_5, user_input_5 = csv_to_json(data_5)

MOCK_DATABASE = {
    "学籍番号とGPA":user_input_1,
    "IRアンケート":user_input_2,
    "成績":user_input_3,
    "授業評価アンケート":user_input_4,
    "学科とGPA":user_input_5
}


@mcp.tool()
def search_csv_data(keyword: str) -> str:
    """
    キーワード（例：設問1）に基づいて、対応するCSVデータのJSON情報を取得します。
    """
    # 辞書からデータを取得
    result = MOCK_DATABASE.get(keyword)

    if result:
        return result
    else:
        return f"エラー：キーワード '{keyword}' に一致するデータが見つかりませんでした。"


if __name__ == "__main__":
    mcp.run(transport="stdio")
