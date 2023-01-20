import os

from dotenv import load_dotenv

load_dotenv()

config_data = {
    "token": os.getenv('TELEGRAM_BOT_API_TOKEN'),
    "site_url": os.getenv('SITE_URL'),
}