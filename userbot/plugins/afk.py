import asyncio
 
from userbot import bot
 
from telethon import functions, types
 
from userbot.events import register
 
isAFK = False
inWait = []
Approved = []
 
@register(outgoing=True, pattern="^[.]afk$")
async def setAFK(e):
  global isAFK
  if isAFK:
    isAFK = False
    await e.edit("**Modalità afk offline**")
  else:
    isAFK = True
    await e.edit("**Modalità afk online!**")
 
@register(outgoing=True, pattern="^[.]approve$")
async def Approve(e):
  global Approved
  if e.is_private and not (await e.get_sender()).bot:
    if e.chat_id in Approved:
      await e.edit("**✅ Questo utente è già approvato.**")
    else:
      Approved.append(e.chat_id)
      await e.edit("**✅ La tua chat è stata appena approvata!**")
 
@register(outgoing=True, pattern="^[.]disapprove$")
async def Disapprove(e):
  global Approved
  if e.is_private and not (await e.get_sender()).bot:
    if e.chat_id in Approved:
      Approved.remove(e.chat_id)
      await e.edit("**❌ La tua chat è stata disattivata!**")
    else:
      await e.edit("**❌ Questo utente non è approvato.**")
 
@register(incoming=True)
async def AFK(e):
  global isAFK, Approved
  if isAFK:
    if e.is_private and not (await e.get_sender()).bot:
      if not e.chat_id in Approved:
        await e.delete()
        if not e.chat_id in inWait:
          await e.respond(f"**👋Ciao, in questo momento non sono disponibile\n\n✅Aspetta che ti sveglio per approvarti la chat\n\n🤐Solo un messaggio ogni 10 secondi verrà salvato quindi spammare non ti servirà a nulla\n\n📩il tuo messaggio:\n{e.text}**")
          inWait.append(e.chat_id)
          await asyncio.sleep(10)
          inWait.remove(e.chat_id)