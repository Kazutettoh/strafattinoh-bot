"""COMMAND : alive. """
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
    await alive.edit("**▬▬▬▬ ❴✪❵ SYSTEM ❴✪❵ ▬▬▬▬**\n\n"
                     "**➖ Telethon: 7.0.1**\n**➖ Python: 3.8.0**\n"
                     "**ℹ️ UPDATE: @IOIIIOIIIOI\n"
                     "**➖ CPU: Qualcomm Snapdragon 855+\n**"
                     f"**👤 USER**: {DEFAULTUSER}\n\n"
                     "**▬▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬▬**")