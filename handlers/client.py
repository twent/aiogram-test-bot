import time
import logging
import asyncio

from aiogram import types
from aiogram.types import ChatActions

from handlers.types import MessageType
from messages import text
from bot import dispatcher, bot
from keyboards import client as client_keyboard

# Обработка команды start
@dispatcher.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    logging.info(f'{time.asctime()}: {user_id=} {user_full_name=}')

    await send_answer(message, text['welcome'].format(user_full_name), markup=client_keyboard.main)

# Задать вопрос
@dispatcher.message_handler(text_contains="Задать вопрос")
async def help(message: types.Message):
    await send_answer(message, text['answer_waiting'], markup=client_keyboard.main)

# О Нас
@dispatcher.message_handler(text_contains="О Нас")
async def about(message: types.Message):
    await send_answer(message, text['about'], markup=client_keyboard.main, delete=True)

# Сайт
@dispatcher.message_handler(text_contains="Перейти на сайт")
async def site_link(message: types.Message):
    await send_answer(message, text['link'], markup=client_keyboard.site_url, delete=True)

# По-умолчанию
@dispatcher.message_handler(content_types="text")
async def default_answer(message: types.Message):
    await send_answer(message, text['default_answer'], "reply", client_keyboard.main)

# Базовая функция для ответа
async def send_answer(message: types.Message, answer="", message_type: MessageType = "answer", markup=None, sleep=2, delete=False):
    try:
        await asyncio.sleep(sleep-1)
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        await asyncio.sleep(sleep)
        # Calling message.reply or message.answer method with or w/o markup 
        await getattr(message, message_type)(answer, reply_markup=markup) if markup else await getattr(message, message_type)(answer)
        if delete == True:
            await message.delete()
    except Exception as e:
        print(e)
