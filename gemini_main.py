import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# 利用可能なモデルを取得
model_id = "gemini-2.0-flash"  # Gemini 2.0 FlashモデルID
model = genai.GenerativeModel(model_id)

# テキスト生成
commandset = "「Go to the 【部屋名】, grasp the 【物体名】 on the 【場所名】 and place it on the 【場所名】.」「Go to the 【部屋名】, grasp the 【物体名】 on the 【場所名】 and give it to 【人物名】.」「Tell me how many 【物体カテゴリー名】 there are on the 【場所名】.」「Tell me how many people in the 【部屋名】 are 【ポーズ】.」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and follow (him | her).」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and guide (him | her) to the 【場所名】.」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and answer (his | her) question.」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and ask (him | her) 【質問】.」"
input_text = input("入力してください:")
# prompt = f"以下のコマンドセットを参考にして、次の文章と一番意味が似ているコマンドセットを抽出し、どの名称が次の文章中のどれと一致するかそれぞれ明示し、その文章のように出力してください。\n\n{commandset}\n\n{input_text}"
prompt = f"次の文章の行動をシーケンス分けしてください。\n\n{input_text}"
response = model.generate_content(prompt)
# 結果を表示
print(response.text)
# print(f"Generated Text: {response.text}")