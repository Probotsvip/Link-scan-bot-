from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.whitelist import add_whitelist, remove_whitelist, list_whitelist
from database.settings import set_punishment, get_punishment

@Client.on_message(filters.command("whitelist") & filters.group)
async def whitelist_user(bot, message: Message):
    if not message.from_user or not message.from_user.id in [OWNER_ID] + message.chat.admins:
        return await message.reply("🚫 Only admins can use this.")

    if not message.reply_to_message:
        return await message.reply("Reply to user to whitelist.")

    user_id = message.reply_to_message.from_user.id
    await add_whitelist(message.chat.id, user_id)
    await message.reply("✅ User whitelisted!")

@Client.on_message(filters.command("settings") & filters.group)
async def settings_menu(bot, message: Message):
    action = await get_punishment(message.chat.id)
    await message.reply(f"🛠 Current punishment for link detection: **{action.upper()}**")

@Client.on_message(filters.command("setpunishment") & filters.group)
async def change_punishment(bot, message: Message):
    if not message.from_user or not message.from_user.id in [OWNER_ID] + message.chat.admins:
        return await message.reply("🚫 Only admins can use this.")
    
    args = message.text.split()
    if len(args) < 2 or args[1] not in ["ban", "mute"]:
        return await message.reply("Usage: /setpunishment [ban|mute]")

    await set_punishment(message.chat.id, args[1])
    await message.reply(f"✅ Punishment changed to {args[1].upper()}")
