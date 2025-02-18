"""
General configuration
"""

import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Telegram bot configuration
TOKEN = os.getenv("TOKEN", "")
USE_WEBHOOK_BOT = os.getenv("USE_WEBHOOK_BOT", "False").lower() in ["true", "1", "yes"]
WEBHOOK_BOT_URL = os.getenv("WEBHOOK_BOT_URL", "https://")
WEBHOOK_BOT_PATH = os.getenv("WEBHOOK_BOT_PATH", "")
WEBHOOK_BOT_PORT = int(os.getenv("WEBHOOK_BOT_PORT", "0"))
WEBHOOK_BOT_CERT = os.getenv("WEBHOOK_BOT_CERT", "")
WEBHOOK_BOT_KEY = os.getenv("WEBHOOK_BOT_KEY", "")

# Internationalization (i18n) settings
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")

# Database configuration
DB_NAME = os.getenv("DB_NAME", "db.sqlite3")
DB_PATH = os.getenv("DB_PATH", "./database")

# Admin user configuration
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "-1"))

# Logging configuration
DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "yes"]
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/jakanode_bot.log")

# Service and Deploy
SERVICE_NAME = os.getenv("SERVICE_NAME", "jakanode-bot")
# USER_NAME = os.getenv("USER", os.getlogin())
USER_NAME = os.getenv("USER", "")
DEV_DIR = os.getenv("DEV_DIR", f"/home/{USER_NAME}/jakanode-bot")
PROD_DIR = os.getenv("PROD_DIR", "/opt/jakanode-bot")

# Donations
DONATION_LN_ADDRESS = os.getenv("DONATION_LN_ADDRESS", "jakanode@lnurl")
DONATION_LN_URL = os.getenv("DONATION_LN_URL", "https://jakanode.lnurl")
