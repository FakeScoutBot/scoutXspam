from telethon import events, Button
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl, ACTIVE_HANDLERS
)

# Help Menu Constants
HELP_STRING = (
    "**𖤍 ғᴇᴀʀʟᴇss sᴘᴀᴍ ʜᴇʟᴘ ᴍᴇɴᴜ 𖤍**\n\n"
    "» ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ\n"
    "» **ᴅᴇᴠᴇʟᴏᴘᴇʀ**: @II_FEARLESS_KING_II"
)

HELP_BUTTON = [
    [Button.inline("• ꜱᴘᴀᴍ •", data="spam"), Button.inline("• ʀᴀɪᴅ •", data="raid")],
    [Button.inline("• ᴇxᴛʀᴀ •", data="extra")],
    [Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/+v1ubYvri73owZDk9"), Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+LbrMou4T_DFkMmRl")]
]

handlers = ACTIVE_HANDLERS

extra_msg = (
    "**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    "𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**\n"
    f"  1) {hl}ping\n"
    f"  2) {hl}reboot\n"
    f"  3) {hl}sudo <reply to user>  --> Owner Cmd\n"
    f"  4) {hl}logs --> Owner Cmd\n\n"
    "𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**\n"
    f"  1) {hl}echo <reply to user>\n"
    f"  2) {hl}rmecho <reply to user>\n\n"
    "𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**\n"
    f"  1) {hl}leave <group/chat id>\n"
    f"  2) {hl}leave : Type in the Group bot will auto leave that group\n\n"
    "**© @II_FEARLESS_KING_II**"
)

raid_msg = (
    "**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    "𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**\n"
    f"  1) {hl}raid <count> <username>\n"
    f"  2) {hl}raid <count> <reply to user>\n\n"
    "𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}rraid <replying to user>\n"
    f"  2) {hl}rraid <username>\n\n"
    "𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}drraid <replying to user>\n"
    f"  2) {hl}drraid <username>\n\n"
    "𝐌𝐑𝐚𝐢𝐝: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}mraid <count> <username>\n"
    f"  2) {hl}mraid <count> <reply to user>\n\n"
    "𝐒𝐑𝐚𝐢𝐝: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}sraid <count> <username>\n"
    f"  2) {hl}sraid <count> <reply to user>\n\n"
    "𝐐𝐑𝐚𝐢𝐝: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}qraid <count> <username>\n"
    f"  2) {hl}qraid <count> <reply to user>\n\n"
    "**© @II_FEARLESS_KING_II**"
)

spam_msg = (
    "**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    "𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**\n"
    f"  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)\n"
    f"  2) {hl}spam <count> <replying any message>\n\n"
    "𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**\n"
    f"  1) {hl}pspam <count>\n\n"
    "𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**\n"
    f"  1) {hl}hang <counter>\n\n"
    "**© @II_FEARLESS_KING_II**"
)

# Event Handler Functions
async def show_help(event):
    if event.sender_id in SUDO_USERS:
        try:
            await event.client.send_file(
                event.chat_id,
                "https://files.catbox.moe/dv0ydx.jpg",
                caption=HELP_STRING,
                buttons=HELP_BUTTON
            )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")

async def helpback(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(HELP_STRING, buttons=HELP_BUTTON)
    else:
        await event.answer("ᴘᴀʜʟᴇ ғᴇᴀʀʟᴇss ᴋɪɴɢ ᴘᴀᴘᴀ sᴇ sᴜᴅᴏ ʟᴇʟᴏ☎️ @II_FEARLESS_KING_II", cache_time=0, alert=True)

async def help_spam(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(spam_msg, buttons=[[Button.inline("< Back", data="help_back")]])

async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg, buttons=[[Button.inline("< Back", data="help_back")]])

async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg, buttons=[[Button.inline("< Back", data="help_back")]])

# Register Event Handlers for Help Command
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))(show_help)
    handler.on(events.CallbackQuery(pattern=r"help_back"))(helpback)
    handler.on(events.CallbackQuery(pattern=r"spam"))(help_spam)
    handler.on(events.CallbackQuery(pattern=r"raid"))(help_raid)
    handler.on(events.CallbackQuery(pattern=r"extra"))(help_extra)

