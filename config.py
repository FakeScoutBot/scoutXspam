import logging
import os
from os import getenv
from telethon import TelegramClient
from dotenv import load_dotenv
from JARVIS.data import FRIDAY

# Load environment variables from .env file
load_dotenv()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Get API credentials from environment variables
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

CMD_HNDLR = getenv("CMD_HNDLR", default=".")
MONGO_DB_URI = getenv("MONGO_DB_URI")
BOT_TOKENS = [
    getenv("BOT_TOKEN", default=None),
    getenv("BOT_TOKEN2", default=None),
    getenv("BOT_TOKEN3", default=None),
    getenv("BOT_TOKEN4", default=None),
    getenv("BOT_TOKEN5", default=None),
    getenv("BOT_TOKEN6", default=None),
    getenv("BOT_TOKEN7", default=None),
    getenv("BOT_TOKEN8", default=None),
    getenv("BOT_TOKEN9", default=None),
    getenv("BOT_TOKEN10", default=None),
]
OWNER_ID = int(getenv("OWNER_ID", default="7044783841"))

# Add SUDO_USERS variable
SUDO_USERS = []
sudo_str = getenv("SUDO_USERS", "")
if sudo_str:
    sudo_users_list = sudo_str.split(",")
    for sudo_user in sudo_users_list:
        if sudo_user.strip():
            SUDO_USERS.append(int(sudo_user))
# Always add OWNER_ID to SUDO_USERS if it's not already there
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

clients = []
for idx, bot_token in enumerate(BOT_TOKENS, start=1):
    if bot_token:
        client = TelegramClient(f'X{idx}', API_ID, API_HASH).start(bot_token=bot_token)
        clients.append(client)
        logging.info(f'Initialized bot X{idx}')

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients[:10]
