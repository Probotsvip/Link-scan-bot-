from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URI)
db = client.linkscan

async def get_punishment(chat_id):
    doc = await db.settings.find_one({"chat_id": chat_id})
    return doc["punishment"] if doc else "mute"

async def set_punishment(chat_id, punishment):
    await db.settings.update_one({"chat_id": chat_id}, {"$set": {"punishment": punishment}}, upsert=True)
