# (©)Codexbotz
# Recode by @KingOf_univers
# t.me/SharingUserbot & t.me/Lunatic0de

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Stop Bots. Join Group https://t.me/Movies_4you for Help"
            )
            sys.exit()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot cannot Take invite link from FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is admin on the Channel, Chat ID of Current F-Subs Channel: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "Stop Bots. Join Group https://t.me/Movies_4you for Help"
                )
                sys.exit()

        if FORCE_SUB_GROUP:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot cannot Take invite link from FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is the admin of the Group, Current F-Subs Group Chat ID: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "Stop Bots. Join Group https://t.me/Movies_4you for Help"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make sure @{self.username} is admin on your DataBase Channel, Current CHANNEL_ID: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Stop Bots. Join Group https://t.me/Movies_4you for Help"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 SUCCESSFULLY ACTIVATED! 🔥]\n\nBOT Created by @{OWNER}\nIf @{OWNER} Needs Help, Please Ask in Group https://t.me/Movies_4you"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
