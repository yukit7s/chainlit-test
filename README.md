# chainlit-test

## 利用方法
* 環境
  * Python 3.8以上
  * pip
  * venv

* 事前に Azure OpenAI などで LLM のモデルを作成し、エンドポイント、APIキー、モデルIDを取得してください。

```sh
git clone https://github.com/yukit7s/chainlit-test.git
cd chainlit-test

# 環境変数の設定
vim .env
# AZURE_OPENAI_ENDPOINT = "{YOUR-ENDPOINT}"
# AZURE_OPENAI_API_KEY = "{YOUR-API-KEY}"
# AZURE_OPENAI_MODEL_ID = "gpt-4o"
# AZURE_OPENAI_API_VERSION = "2024-07-01-preview"

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Chainlit のテスト起動
chainlit hello
# Ctrl + C で終了

# アプリの実行
chainlit run app.py -w
# Ctrl + C で終了

deactivate
```


