# (©)Codexbotz
# Recode by @KingOf_univers
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command("batch"))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(
                text="<i><b>Pʟᴇᴀsᴇ Fᴏʀᴡᴀʀᴅ Tʜᴇ Fɪʀsᴛ Mᴇssᴀɢᴇ/Fɪʟᴇ Fʀᴏᴍ Tʜᴇ DᴀᴛᴀBᴀsᴇ Cʜᴀɴɴᴇʟ. (Fᴏʀᴡᴀʀᴅ Wɪᴛʜ Qᴜᴏᴛᴇ)</b></i>\n\n<i><b>Oʀ Sᴇɴᴅ Pᴏsᴛ Lɪɴᴋ Fʀᴏᴍ Mʏ Cʜᴀɴɴᴇʟ Dᴀᴛᴀʙᴀsᴇ</b></i>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        await first_message.reply(
            "❌ <i><b>Eʀʀᴏʀ</b></i>\n\n<i><b>Tʜɪs Fᴏʀᴡᴀʀᴅᴇᴅ Pᴏsᴛ Is Nᴏᴛ Fʀᴏᴍ Mʏ Cʜᴀɴɴᴇʟ Dᴀᴛᴀʙᴀsᴇ</b></i>",
            quote=True,
        )
        continue

    while True:
        try:
            second_message = await client.ask(
                text="<i><b>Pʟᴇᴀsᴇ Fᴏʀᴡᴀʀᴅ Tʜᴇ Lᴀsᴛ Mᴇssᴀɢᴇ/Fɪʟᴇ Fʀᴏᴍ Tʜᴇ DᴀᴛᴀBᴀsᴇ Cʜᴀɴɴᴇʟ. (Fᴏʀᴡᴀʀᴅ Wɪᴛʜ Qᴜᴏᴛᴇ)</b></i>\n\n<i><b>Oʀ Sᴇɴᴅ Pᴏsᴛ Lɪɴᴋ Fʀᴏᴍ Mʏ Cʜᴀɴɴᴇʟ Dᴀᴛᴀʙᴀsᴇ</b></i>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        await second_message.reply(
            "❌ <i><b>Eʀʀᴏʀ</b></i>\n\n<i><b>Tʜɪs Fᴏʀᴡᴀʀᴅᴇᴅ Pᴏsᴛ Is Nᴏᴛ Fʀᴏᴍ Mʏ Cʜᴀɴɴᴇʟ Dᴀᴛᴀʙᴀsᴇ</b></i>",
            quote=True,
        )
        continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔁 Sʜᴀʀᴇ Lɪɴᴋ", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await second_message.reply_text(
        f"<i><b>Fɪʟᴇ Sʜᴀʀɪɴɢ Lɪɴᴋ Sᴜᴄᴄᴇssғᴜʟʟʏ Cʀᴇᴀᴛᴇᴅ:</b></i>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command("genlink"))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(
                text="<i><b>Pʟᴇᴀsᴇ Fᴏʀᴡᴀʀᴅ Mᴇssᴀɢᴇs Fʀᴏᴍ Tʜᴇ DᴀᴛᴀBᴀsᴇ Cʜᴀɴɴᴇʟ. (Fᴏʀᴡᴀʀᴅ Wɪᴛʜ Qᴜᴏᴛᴇs)</b></i>\n\n<b>Oʀ Sᴇɴᴅ Pᴏsᴛ Lɪɴᴋ Fʀᴏᴍ Mʏ Cʜᴀɴɴᴇʟ Dᴀᴛᴀʙᴀsᴇ</b></i>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        await channel_message.reply(
            "❌ <i><b>Eʀʀᴏʀ</b></i>\n\n<i><b>Tʜɪs Fᴏʀᴡᴀʀᴅᴇᴅ Pᴏsᴛ Is Nᴏᴛ Fʀᴏᴍ Mʏ Cʜᴀɴɴᴇʟ Dᴀᴛᴀʙᴀsᴇ</b></i>",
            quote=True,
        )
        continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔁 Sʜᴀʀᴇ Lɪɴᴋ", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await channel_message.reply_text(
        f"<i><b>Fɪʟᴇ Sʜᴀʀɪɴɢ Lɪɴᴋ Sᴜᴄᴄᴇssғᴜʟʟʏ Cʀᴇᴀᴛᴇᴅ:</b></i>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )
