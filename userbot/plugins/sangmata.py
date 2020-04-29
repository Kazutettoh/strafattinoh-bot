import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
import asyncio
from userbot import CMD_HELP, ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "I'M STUPID"



@borg.on(admin_cmd(pattern=("sg ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
      return
   chat = "@SangMataInfo_bot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
      return
   await event.edit(f"`{DEFAULTUSER}:`**Ricerca Storico...**")
   async with borg.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
            await borg.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("```Please sblocca @Sangmatainfo_bot ```")
            return
         if response.text.startswith("Forward"):
            await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
         else: 
            await event.edit(f"{response.message.message}")



@borg.on(admin_cmd(pattern=("gid ?(.*)")))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Ricerca Info...**")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please sblocca @getidsbot ```")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else: 
             await event.edit(f"{response.message.message}")
