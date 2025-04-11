from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/+LbrMou4T_DFkMmRl"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+LbrMou4T_DFkMmRl")
    ],
    [Button.url("• ʀᴇᴘᴏ •", "https://t.me/+LbrMou4T_DFkMmRl")]
]

# Define a list of handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

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
                f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [《●꯭𝐅꯭ᴇ꯭᧘꯭ʀ꯭ʟᴇ꯭ຮ꯭ຮ꯭ 𝐊꯭ι𝗇꯭ɢ꯭❤️‍🔥꯭々꯭»꯭™꯭⁷⁷⁷꯭●》](https://t.me/II_FEARLESS_KING_II)**\n\n"
                f"» **Fearless V2 :** `M 1.8.31`\n"
                f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
                f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
            )

            await event.client.send_file(
                event.chat_id,
                "https://github.com/doraemon890/JARVIS-X-SPAM/assets/155803358/f30a5777-9823-45d0-9860-342eceadb774",
                caption=TEXT,
                buttons=START_BUTTON
            )
