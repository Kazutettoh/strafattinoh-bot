"""Check if userbot alive. """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "senza nome"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**🔰🔗 USERBOT 🔗🔰**\n\n"
                     "**➖ Telethon: 7.0.1**\n**➖ Python: 3.8.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**ℹ️ UPDATE: @IOIIIOIIIOI\n➖ CREATORE BOT: [SnapDragon7410](tg://user?id=719877937)**\n"
                     "**➖ CPU: Qualcomm Snapdragon 855+\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n🔰🔗 DATI USER 🔗🔰\n\n**"
                     f"**👤 USER**: {DEFAULTUSER}")