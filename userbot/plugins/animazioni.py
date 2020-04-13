"""
Available Commands:
.sex
.fuck
.kiss
.pornhub
.love
.sexy"""


from telethon import events

from userbot.utils import admin_cmd

import asyncio



@borg.on(admin_cmd(pattern=f"fuck", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "fuck":

        await event.edit(input_str)

        animation_chars = [

            "👉       ✊️",

            "👉     ✊️",

            "👉  ✊️",

            "👉✊️💦"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(admin_cmd(pattern=f"sex", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "sex":

        await event.edit(input_str)

        animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵👼👰"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(admin_cmd(pattern=f"kiss", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "kiss":

        await event.edit(input_str)

        animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵💋👰"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(admin_cmd(pattern="pornhub"))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "pornhub":

        await event.edit(input_str)

        animation_chars = [

            "P_",

            "PO_",

            "POR_",

            "PORN_",
            
            "PORNH_",
            
            "PORNHU_",
            
           "PORNHUB_", 
           
           "PORNHUB",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])



@borg.on(admin_cmd(pattern="love"))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "love":

        await event.edit(input_str)

        animation_chars = [

            "L_",

            "LO_",

            "LOV_",
            
            "LOVE_",
            
            "LOVE❤",
            

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])



@borg.on(admin_cmd(pattern="sexy"))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "sexy":

        await event.edit(input_str)

        animation_chars = [

            "S_",

            "SE_",

            "SEX_",

            "SEXY_",
            
            "SEXY👄_",
            
            "SEXY👄",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
