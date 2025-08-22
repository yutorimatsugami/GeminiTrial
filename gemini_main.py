import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# 利用可能なモデルを取得
model_id = "gemini-2.5-flash"  # Gemini 2.5 FlashモデルID
model = genai.GenerativeModel(model_id)

# 指示作成例その１：コマンドセットとの一致
# commandset = "「Go to the 【部屋名】, grasp the 【物体名】 on the 【場所名】 and place it on the 【場所名】.」「Go to the 【部屋名】, grasp the 【物体名】 on the 【場所名】 and give it to 【人物名】.」「Tell me how many 【物体カテゴリー名】 there are on the 【場所名】.」「Tell me how many people in the 【部屋名】 are 【ポーズ】.」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and follow (him | her).」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and guide (him | her) to the 【場所名】.」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and answer (his | her) question.」「Go to the 【部屋名】, find 【人物名】 at the 【場所名】 and ask (him | her) 【質問】.」"
# input_text = input("入力してください:")
# prompt = f"以下のコマンドセットを参考にして、次の文章と一番意味が似ているコマンドセットを抽出し、どの名称が次の文章中のどれと一致するかそれぞれ明示し、その文章のように出力してください。\n\n{commandset}\n\n{input_text}"

# 指示作成例その２：行動シーケンスの分割
# input_text = input("入力してください:")
# prompt = f"次の文章の行動をシーケンス分けしてください。\n\n{input_text}＋このときシーケンス分けした結果のみを箇条書きで英語で出力すること+順番をロボットが実行する順番で出力すること+各行動の前に番号をつけること+各行動の後に「.」をつけること"

# 指示作成例その３：ロボット学会学術講演会の論文の実験で使ったchatGPTのプロンプト
# HSR_GPT_Prompt.txtの内容を読み込む
prompt_file_path = "HSR_GPT_Prompt.txt"
with open(prompt_file_path, "r", encoding="utf-8") as file:
    prompt = file.read()
    
response = model.generate_content(prompt)
# 結果を表示
print(response.text)
# print(f"Generated Text: {response.text}")