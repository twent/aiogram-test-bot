from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import config_data

storage = MemoryStorage()
bot = Bot(token=config_data['token'])
dispatcher = Dispatcher(bot, storage)
