import sys
import heroku3
import asyncio
import base64
from datetime import datetime
from os import execl, getenv

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    OWNER_ID, SUDO_USERS, HEROKU_APP_NAME,
    HEROKU_API_KEY, CMD_HNDLR as hl, ACTIVE_HANDLERS
)
from JARVIS.data import FRIDAY

ECHO = []

# List of handlers - only use active ones
handlers = ACTIVE_HANDLERS

# Function to handle ping command
async def ping(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        jarvis = await event.reply("ᴥ︎︎︎ 𝗙𝗘𝗔𝗥𝗟𝗘𝗦𝗦 𝗞𝗜𝗡𝗚 𝗜𝗦 ✔︎")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await jarvis.edit(f"[𝗙𝗘𝗔𝗥𝗟𝗘𝗦𝗦 𝗞𝗜𝗡𝗚 𝗜𝗦 𝗥𝗘𝗔𝗗𝗬 𝗧𝗢  ](https://t.me/+v1ubYvri73owZDk9)[𝗙𝗨𝗖𝗞 𝗛𝗔𝗧𝗘𝗥𝗦 🥀](https://t.me/+LbrMou4T_DFkMmRl)🤖\n» `{mp} ᴍꜱ`")

# Function to handle reboot command
async def restart(event):
    if event.sender_id in SUDO_USERS:
        await event.reply("`ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ`")
        for handler in handlers:
            try:
                await handler.disconnect()
            except Exception:
                pass
        execl(sys.executable, sys.executable, *sys.argv)

# Function to add sudo user
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default="")
        ok = await event.reply("» __Fearless King Ka Ek Beta Aur Add Ho rha hai.__")
        target = ""
        
        if HEROKU_APP_NAME is None:
            await ok.edit("`[HEROKU]:\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        
        app = Heroku.app(HEROKU_APP_NAME)
        heroku_var = app.config()
        
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ʀᴇᴘʟʏ ᴜsᴇʀ ᴏʀ ᴜsᴇ ᴀᴅᴅᴍᴜʟᴛɪsᴜᴅᴏ ғᴜɴᴄᴛɪᴏɴ")
            return

        if str(target) in sudousers:
            await ok.edit("ʏᴇ ᴛᴏʜ ғᴇᴀʀʟᴇss ᴋɪɴɢ ᴋᴀ ʜɪ ʙᴀᴄʜᴀ ʜᴀɪ ")
        else:
            newsudo = f"{sudousers} {target}".strip()
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ADD KAR DIYE HAI SUDO..BOT RESTART HO RHA HAI`")
            heroku_var["SUDO_USERS"] = newsudo
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ᴏɴʟʏ ғᴇᴀʀʟᴇss ᴋɪɴɢ ᴄᴀɴ ᴀᴅᴅ sᴜᴅᴏ ᴜsᴇʀs..")

# Function to remove sudo user
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default="")
        ok = await event.reply("ᴛʜɪs ɢᴜʏ ɪs ɴᴏᴛ ᴅᴇʀᴠᴇs ᴛʜɪs ʙᴏᴛ.\n\n`ғᴜᴄᴋ ɪᴛ...`")
        target = ""
        
        if HEROKU_APP_NAME is None:
            await ok.edit("`[HEROKU]:\nPlease set up your HEROKU_APP_NAME`")
            return
        
        app = Heroku.app(HEROKU_APP_NAME)
        heroku_var = app.config()
        
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("ʀᴇᴘʟʏ ɪᴛ ᴏʀ ᴍᴇɴᴛɪᴏɴ ɪᴅ ᴏғ ᴜsᴇʀ")
            return
        
        if str(target) not in sudousers:
            await ok.edit("ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ")
        else:
            new_sudo_users = " ".join([user for user in sudousers.split() if user != str(target)])
            await ok.edit(f"Removed sudo user: `{target}`")
            heroku_var["SUDO_USERS"] = new_sudo_users
    else:
        await event.reply("ᴏɴʟʏ ғᴇᴀʀʟᴇss ᴋɪɴɢ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ ᴜsᴇʀs..")

# Function to show sudo users
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "ᴋɪᴅᴢᴢ ᴏғ ᴛʜᴇ **ғᴇᴀʀʟᴇss ᴋɪɴɢ**:\n"
        for user_id in SUDO_USERS:
            sudo_users_list += f"- {user_id}\n"
        await event.reply(sudo_users_list)
    else:
        await event.reply("ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ ᴄᴀɴ ᴏɴʟʏ ᴘᴇʀғᴏʀᴍ ʙʏ ғᴇᴀʀʟᴇss ᴋɪɴɢ.")

# Function to add multiple sudo users
async def addmultisudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default="")
        ok = await event.reply("ᴀᴅᴅɪɴɢ ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀs...")
        
        if HEROKU_APP_NAME is None:
            await ok.edit("`[HEROKU]:\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        
        app = Heroku.app(HEROKU_APP_NAME)
        heroku_var = app.config()

        new_sudo_users = sudousers.split() if sudousers else []

        try:
            # Extract user IDs from the message directly
            target_ids = [int(x) for x in event.pattern_match.group(1).split()]
        except:
            await ok.edit("Error processing the user IDs.")
            return

        # Remove duplicate user IDs
        target_ids = list(set(target_ids))

        # Add new user IDs to the list of sudo users
        new_sudo_users.extend(str(user_id) for user_id in target_ids if str(user_id) not in new_sudo_users)
        
        # Update Heroku configuration variable
        new_sudo_users_str = ' '.join(new_sudo_users)
        heroku_var["SUDO_USERS"] = new_sudo_users_str
        
        await ok.edit(f"Added {len(target_ids)} new sudo users.")
    elif event.sender_id in SUDO_USERS:
        await event.reply("ᴏɴʟʏ ғᴇᴀʀʟᴇss ᴋɪɴɢ ᴄᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪsᴜᴅᴏ ᴜsᴇʀs ᴀᴛ ᴀ ᴛɪᴍᴇ.")

# Register event handlers - only for active handlers
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))(ping)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))(restart)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))(addsudo)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))(removesudo)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))(show_sudo_users)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))(addmultisudo)
