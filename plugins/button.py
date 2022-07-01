# Credits: @KingOf_univers
# FROM File-Store-Bot <https://github.com/TG-SURAJ/File-Store-Bot/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="📌 Aʙᴏᴜᴛ Mᴇ", callback_data="about"),
                InlineKeyboardButton(text="Cʟᴏsᴇ ✗", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="⚔️ Gʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="📌 Aʙᴏᴜᴛ Mᴇ ", callback_data="about"),
                InlineKeyboardButton(text="Cʟᴏsᴇ ✗", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="💫 Cʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="📌 Aʙᴏᴜᴛ Mᴇ ", callback_data="about"),
                InlineKeyboardButton(text="Cʟᴏsᴇ ✗", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="📌 Aʙᴏᴜᴛ Mᴇ", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="💫 Cʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="⚔️ Gʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="Cʟᴏsᴇ ✗", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="⚔️ Jᴏɪɴ Gʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Tʀʏ Aɢᴀɪɴ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="💫 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Tʀʏ Aɢᴀɪɴ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="💫 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="⚔️ Jᴏɪɴ Gʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Tʀʏ Aɢᴀɪɴ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
