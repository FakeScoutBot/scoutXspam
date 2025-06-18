from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, ACTIVE_HANDLERS

START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/+v1ubYvri73owZDk9"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+V2fhBCp2c1Y0NjI9")
    ],
    [Button.url("• ʀᴇᴘᴏ •", "https://t.me/III_FEARLESS_KING_III")]
]

# Use only active handlers
handlers = ACTIVE_HANDLERS

# Register event handlers
for handler in handlers:
    @handler.on(events.NewMessage(pattern="/start"))
    async def start(event):
        if event.is_private:
            ANNIE = await event.client.get_me()
            bot_name = ANNIE.first_name
            bot_id = ANNIE.id

            TEXT = (
                f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n"
                f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n━━━━━━━━━━━━━━━━━━━\n\n"
                f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [《●꯭𝐅꯭ᴇ꯭᧘꯭ʀ꯭ʟᴇ꯭ຮ꯭ຮ꯭ 𝐊꯭ι𝗇꯭ɢ꯭❤️‍🔥꯭々꯭»꯭™꯭⁷⁷⁷꯭●》](https://t.me/III_FEARLESS_KING_III)**\n\n"
                f"» **ғᴇᴀʀʟᴇss V2 :** `M 1.8.31`\n"
                f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
                f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
            )

            await event.client.send_file(
                event.chat_id,
                "https://files.catbox.moe/dv0ydx.jpg",
                caption=TEXT,
                buttons=START_BUTTON
            )
