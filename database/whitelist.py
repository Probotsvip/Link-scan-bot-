from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URI)
db = client.linkscan

async def is_whitelisted(chat_id, user_id):
    return await db.whitelist.find_one({"chat_id": chat_id, "user_id": user_id}) is not None

async def add_whitelist(chat_id, user_id):
    await db.whitelist.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {}}, upsert=True)

async def remove_whitelist(chat_id, user_id):
    await db.whitelist.delete_one({"chat_id": chat_id, "user_id": user_id})

async def list_whitelist(chat_id):
    return await db.whitelist.find({"chat_id": chat_id}).to_list(length=100)
