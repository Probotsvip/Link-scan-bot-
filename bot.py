from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_TOKEN, API_ID, API_HASH
from handlers import group_events, commands

bot = Client(
    "LinkScanBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "handlers"},
)

if __name__ == "__main__":
    print("🤖 LinkScanBot Started!")
    bot.run()
