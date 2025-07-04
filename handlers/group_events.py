from pyrogram import Client, filters
from pyrogram.types import Message
from utils.detection import contains_link, bio_contains_link
from database.whitelist import is_whitelisted
from database.settings import get_punishment

@Client.on_message(filters.group & filters.text)
async def scan_links(bot, message: Message):
    user = message.from_user
    if not user or await is_whitelisted(message.chat.id, user.id):
        return

    if contains_link(message.text):
        action = await get_punishment(message.chat.id)
        await message.delete()
        if action == "ban":
            await bot.ban_chat_member(message.chat.id, user.id)
        elif action == "mute":
            await bot.restrict_chat_member(
                message.chat.id, user.id, permissions={"can_send_messages": False}
            )
        await message.reply(f"🚨 {user.mention} sent a link! Action: {action.upper()}")

@Client.on_chat_member_updated()
async def scan_bio(bot, member_update):
    user = member_update.new_chat_member.user
    if user.is_bot:
        return

    if await is_whitelisted(member_update.chat.id, user.id):
        return

    if bio_contains_link(user.bio or ""):
        action = await get_punishment(member_update.chat.id)
        if action == "ban":
            await bot.ban_chat_member(member_update.chat.id, user.id)
        elif action == "mute":
            await bot.restrict_chat_member(
                member_update.chat.id, user.id, permissions={"can_send_messages": False}
            )
