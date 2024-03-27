from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loader import dp, bot
from keyboards import kb_client, kb_direct, kb_docks

async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 
                           '')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(help, commands=['help'])