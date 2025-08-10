# ベースイメージ
FROM python:3.12-slim

# 作業ディレクトリ
WORKDIR /app

# pipをアップデート
RUN pip install --upgrade pip

# 依存関係をコピー
COPY app/requirements.txt .

# ライブラリインストール（詳細ログ付き）
RUN pip install --no-cache-dir -r requirements.txt -v

# アプリコードをコピー
COPY app .

# Flask起動（デバッグON）
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
