"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events
from userbot.utils import admin_cmd

import asyncio


@borg.on(admin_cmd(pattern=f"call", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Chiamata alla sede di Telegram...`",
            "`Chiamata Connessa`",
            "`Telegram: Salve, risponde la sede di Telegram. Chi è lei?`",
            "`Io: Salve sono` @IOIIIOIIIOI ,`Devo parlare con il mio socio ,Pavel Durov`",
            "`User Autorizzato.`",
            "`Chiamata a Pavel Durov` `+6969696969`",
            "`Chiamata Connessa`",  
            "`Io: Banna questo account da Telegram`",
            "`Pavel: Posso sapere chi sei?`",
            "`Io: Yo bro, sono` @IOIIIOIIIOI ",
            "`Pavel: OMG!!! Ma è da tanto che non ci vediamo, bro...\nMi assicurerò io che l'account venga bloccato entro 24 ore.`",
            "`Io: Grazie, a dopo bro.`",
            "`Pavel: Ma va bro, telegram è nostro. Chiamami quando sei libero`",
            "`Io: C'è qualche problema bro?🤔`",
            "`Pavel: Sì bro, c'è un bug in telegram v8.6.9.\nNon sono in grado di risolverlo. Mi, aiuti a correggere il bug?`",
            "`Io: Inviami tutto sul mio Telegram, risolverò il bug.`",
            "`Pavel: Grazie bro \nCi sentiamo :)`",
            "`Chiamata Disconnessa.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
