from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton

from config import config_data
from buttons import labels

# Buttons for ReplyMarkup
question = KeyboardButton(labels['question'])
get_site_link = KeyboardButton(labels['site'])
about = KeyboardButton(labels['about'])

# Buttons for InlineMarkup
link = InlineKeyboardButton(labels['site'], url=config_data['site_url'])

# Keyboards
main = ReplyKeyboardMarkup(resize_keyboard=True).row(question, get_site_link, about)
site_url = InlineKeyboardMarkup(row_width=2).row(link)
