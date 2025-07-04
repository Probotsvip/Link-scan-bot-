import os

API_ID = int(os.environ.get("API_ID", "123456"))  # Your Telegram API ID
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

MONGO_URI = os.environ.get("MONGO_URI", "your_mongo_db_uri")
OWNER_ID = int(os.environ.get("OWNER_ID", "7168729089"))
