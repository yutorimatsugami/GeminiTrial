import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# 利用可能なモデルをリストアップ
models = genai.list_models()
# ログファイルに保存
log_file_path = "models/log.txt"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)  # ディレクトリが存在しない場合は作成

with open(log_file_path, "w", encoding="utf-8") as log_file:
    for model in models:
        log_file.write(f"{model}\n")  # モデルオブジェクト全体を保存
        # log_file.write(f"Model ID: {model.id}, Description: {model.description}\n")  # 必要に応じて修正

# 完了メッセージ
print("モデル一覧の取得とログファイルへの保存が完了しました。")