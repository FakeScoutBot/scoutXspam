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

# Create clients for available bot tokens
clients = []
for idx, bot_token in enumerate(BOT_TOKENS, start=1):
    if bot_token:
        client = TelegramClient(f'X{idx}', API_ID, API_HASH).start(bot_token=bot_token)
        clients.append(client)
        logging.info(f'Initialized bot X{idx}')

# Ensure we have at least one client
if not clients:
    raise ValueError("At least one BOT_TOKEN is required!")

# Create variables X1-X10, filling with None for missing clients
X1 = clients[0] if len(clients) > 0 else None
X2 = clients[1] if len(clients) > 1 else None
X3 = clients[2] if len(clients) > 2 else None
X4 = clients[3] if len(clients) > 3 else None
X5 = clients[4] if len(clients) > 4 else None
X6 = clients[5] if len(clients) > 5 else None
X7 = clients[6] if len(clients) > 6 else None
X8 = clients[7] if len(clients) > 7 else None
X9 = clients[8] if len(clients) > 8 else None
X10 = clients[9] if len(clients) > 9 else None

# Create a list of only active handlers for use in other modules
ACTIVE_HANDLERS = [client for client in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10] if client is not None]

print(f"✅ Successfully initialized {len(ACTIVE_HANDLERS)} bot client(s)")
