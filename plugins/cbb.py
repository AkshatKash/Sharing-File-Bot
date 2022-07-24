# (©)Codexbotz
# Recode by @KingOf_univers
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<i><b>Aʙᴏᴜᴛ Tʜɪs ʙᴏᴛ:\n\n@{client.username} Is A Tᴇʟᴇɢʀᴀᴍ Bᴏᴛ Tᴏ Sᴛᴏʀᴇ Pᴏsᴛs Oʀ Fɪʟᴇs Tʜᴀᴛ Cᴀɴ Bᴇ Aᴄᴄᴇssᴇᴅ Vɪᴀ Sᴘᴇᴄɪᴀʟ Lɪɴᴋs.\n\n○ Cʀᴇᴀᴛᴏʀ : @{OWNER}\n○ Cʜᴀɴɴᴇʟ: @AkshatStudios2\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ: @MoviesRequestingGroup</b></i>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Cʟᴏsᴇ ✗", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
