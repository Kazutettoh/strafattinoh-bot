from datetime import datetime
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from userbot import CMD_HELP
from userbot.events import register, errors_handler

@register(pattern=".chatinfo(?: |$)(.*)", outgoing=True)
@errors_handler
async def info(event):
    await event.edit("**Info chat...**")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit("`An unexpected error has occurred.`")
    return


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.edit("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.edit("`Channel o supergroup non exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return chat_info


async def fetch_info(chat, event):
    # chat.chats is a list so we use get_entity() to avoid IndexError
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1), 
                                                        add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    # No chance for IndexError as it checks for msg_info.messages first
    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    # Same for msg_info.users
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Deleted Account"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Unknown"
        location = str(e)
    
    #this is some spaghetti I need to change
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restrcited_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    members_online = chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = "<b>Yes</b>" if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup else "No"
    slowmode = "<b>Yes</b>" if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else "No"
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = "<b>Yes</b>" if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted else "No"
    verified = "<b>Yes</b>" if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else "No"
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None
    #end of spaghetti block
    
    if admins is None:
        # use this alternative way if chat.full_chat.admins_count is None, works even without being an admin
        try:
            participants_admins = await event.client(GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                                                            offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = "<b>CHAT INFO:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"{chat_type} nome: {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"Former name: {former_title}\n"
    if username is not None:
        caption += f"{chat_type} type: Public\n"
        caption += f"Link: {username}\n"
    else:
        caption += f"{chat_type} type: Private\n"
    if creator_username is not None:
        caption += f"Founder: {creator_username}\n"
    elif creator_valid:
        caption += f"Creator: <a href=\"tg://user?id={creator_id}\">{creator_firstname}</a>\n"
    if created is not None:
        caption += f"Creato: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"Creator: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"DC ID: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1+sqrt(1+7*exp_count/14))/2)
        caption += f"{chat_type} level: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"View messaggi: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"Messaggi scritti: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"Messages sent: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"Membri: <code>{members}</code>\n"
    if admins is not None:
        caption += f"Admins: <code>{admins}</code>\n"
    if bots_list:
        caption += f"Bot: <code>{bots}</code>\n"
    if members_online:
        caption += f"User online: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"User limitati: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"User bannati: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f"{chat_type} Stickers: <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a>\n"
    caption += "\n"
    if not broadcast:
        caption += f"Slow mode: {slowmode}"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
    if not broadcast:
        caption += f"Supergruppo: {supergroup}\n\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += f"Limitato: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> Platform: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> Reason: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> Text: {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
    	caption += "Scam: <b>Yes</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"Verificato da Telegram: {verified}\n\n"
    if description:
        caption += f"Descrizione: \n<code>{description}</code>\n"
    return caption

CMD_HELP.update({
"chatinfo":
".chatinfo [optional: <reply/tag/chat id/invite link>]\
\nUsage: Gets info of a chat. Some info might be limited due to missing permissions."})



"""Count the Number of Dialogs you have in your Telegram Account
Syntax: .stat"""
from telethon import events
import asyncio
from datetime import datetime
from telethon.tl.types import User, Chat, Channel
from userbot.utils import admin_cmd

import time
from telethon.events import NewMessage
from telethon.tl.custom import Dialog



"""Type `.count` and see Magic."""

@borg.on(admin_cmd(pattern='stat'))
async def stats(event: NewMessage.Event) -> None:  # pylint: disable = R0912, R0914, R0915
    """Command to get stats about the account"""
    waiting_message = await event.edit('`Collecting stats, Wait man`')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog, limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1

            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1

        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1

        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time

    full_name = inline_mention(await event.client.get_me())
    response = f'📌 **Statistiche {full_name}** \n\n'
    response += f'**Chat Totali:** {private_chats} \n'
    response += f'   ★ `User: {private_chats - bots}` \n'
    response += f'   ★ `Bot: {bots}` \n'
    response += f'**Gruppi:** {groups} \n'
    response += f'**Canali:** {broadcast_channels} \n'
    response += f'**Admin in Gruppi:** {admin_in_groups} \n'
    response += f'   ★ `Founder: {creator_in_groups}` \n'
    response += f'   ★ `Admin: {admin_in_groups - creator_in_groups}` \n'
    response += f'**Admin in Canali:** {admin_in_broadcast_channels} \n'
    response += f'   ★ `Founder: {creator_in_channels}` \n'
    response += f'   ★ `Admin: {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'**Unread:** {unread} \n'
    response += f'**Unread Mentions:** {unread_mentions} \n\n'
    response += f'📌 __Editato in:__ {stop_time:.02f}s \n'

    await event.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name
