"""COMMAND : alive. """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "I'M STUPID"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ .alive command, check if the bot is running. """
    await alive.edit("**▬▬▬▬▬ ❴✪❵ SYSTEM ❴✪❵ ▬▬▬▬▬**\n\n"
                     "**➖ Telethon: 7.0.1**\n**➖ Python: 3.8.2**\n"
                     "**➖ CPU: Qualcomm Snapdragon 855+\nℹ️ [UPDATE](https://t.me/IOIIOIIIOIIOI)\n**"
                     f"**👤 USER**: {DEFAULTUSER}\n\n"
                     "▬▬▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬▬▬")
