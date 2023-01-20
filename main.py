from aiogram import executor

from bot import dispatcher
from handlers import client

executor.start_polling(dispatcher, skip_updates=True)