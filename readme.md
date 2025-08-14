# Gemini API テキスト生成プロジェクト

## 概要

このプロジェクトは、GoogleのGemini APIを利用して、特定のコマンドセットに基づいたテキスト生成を行うPythonスクリプトです。ユーザーが入力した自然言語の指示を解釈し、対応するコマンド形式に変換したり、指示内容をシーケンスに分解したりする機能を提供します。


## 主な機能

* **テキスト生成**: ユーザーの入力に基づいて、Geminiモデルがテキストを生成します。
* **コマンド変換**: 入力された文章を、あらかじめ定義されたコマンドセットの中から最も意味が近いものに一致させることができます。
* **行動シーケンスの分割**: 入力された文章が示す行動を、一連のステップに分解します。
* **利用可能モデルのリストアップ**: 使用できるGeminiのモデルを一覧表示し、ログファイルに保存する機能も含まれています。

## 0. リポジトリのクローン
まず、このプロジェクトをローカル環境に複製します。ターミナル（またはコマンドプロンプト）を開き、以下のコマンドを実行してください。

```Bash
# 自分のワークスペースに移動
cd your_ws  
# HTTPS経由でクローン
git clone https://github.com/your-username/your-repository-name.git

# クローンしたディレクトリに移動
cd your-repository-name
```
## 1. 動作環境のセットアップ

プロジェクトを実行するためには、Pythonの仮想環境の構築と、必要なライブラリのインストールが必要です。

### 仮想環境の構築

まず、プロジェクト用の仮想環境を作成します。

```bash
# 'genv'という名前で仮想環境を作成(gemini environmentの略)
python -m venv genv
```

次に、作成した仮想環境を有効化します。

**Windowsの場合:**

```bash
genv\Scripts\activate
```

**Linux/Macの場合:**

```bash
source genv/bin/activate
```

### ライブラリのインストール

`requirements.txt`ファイルを使用して、必要なライブラリを一括でインストールします。

```bash
pip install -r requirements.txt
```

インストールされるライブラリは以下の通りです。
* `python-dotenv`
* `google-generativeai`

## 2. APIキーの設定

次に、Google Gemini APIを利用するためのAPIキーを設定します。

1.  プロジェクトのルートディレクトリに `.env` という名前のファイルを作成します。
2.  `.env` ファイルに、お使いのGoogle APIキーを以下のように記述します。

    ![.env file content](https://storage.googleapis.com/generativeai-assets/user_uploaded_files/image_c967ac.png)

    ```
    # API key for Google Gemini
    GOOGLE_API_KEY="ここにあなたのAPIキーを貼り付けます"
    ```

**注意**: `.env` ファイルは、APIキーなどの機密情報を含みます。`.gitignore`ファイルに`.env`が記載されていることを確認し、Gitリポジトリにコミットしないようにしてください。

## 3. スクリプトの実行

### メインスクリプトの実行

`gemini_main.py` を実行すると、コンソールにプロンプトが表示され、テキストを入力するよう求められます。テキストを入力すると、Geminiモデルが応答を生成し、結果が出力されます。

```bash
python gemini_main.py
```

**実行例:**

```
入力してください:リビングルームに行って、テーブルの上にあるリンゴを取って、私にください。
```

スクリプト内の`prompt`変数を変更することで、Geminiに与える指示をカスタマイズできます。

**コマンドセットとの一致（例）:**
```python
prompt = f"以下のコマンドセットを参考にして、次の文章と一番意味が似ているコマンドセットを抽出し、どの名称が次の文章中のどれと一致するかそれぞれ明示し、その文章のように出力してください。\n\n{commandset}\n\n{input_text}"
```

**行動シーケンスの分割（例）:**
```python
prompt = f"次の文章の行動をシーケンス分けしてください。\n\n{input_text}"
```

### 利用可能モデルのリストアップ

`gemini_avaliable_model_list.py` を実行すると、現在利用可能なすべてのGeminiモデルが`models/log.txt`に出力されます。

```bash
python gemini_avaliable_model_list.py
```

これにより、`gemini_main.py` で使用する`model_id`を他のモデルに変更する際の参考にすることができます。

## 仮想環境の終了

作業が終了したら、以下のコマンドで仮想環境を無効化できます。

```bash
deactivate
```