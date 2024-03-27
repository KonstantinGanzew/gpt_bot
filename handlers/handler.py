import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
import keyboards.inline.choice_buttons as key
import keyboards.inline.callback_datas as call_datas
import keyboards.keyboard as button
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Обработчик команды start
@dp.message_handler(Command('start'))
async def show_menu(message: Message):
    await bot.send_message(chat_id=message.chat.id, 
                           text='Привет, я тот кто способен помочь тебе...\nВсего пару уточнений.', 
                           reply_markup=key.menu_keyboard)

# Первый пункт    
@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu='next'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Я бот OpenAi,\n\
                                 создан @kureed для облегчения жизни, так как всякие ресурсы OpenAi либо имеют бешаные\
                                 цены, либо работают 1 день, было решено взять свой токен и попробовать общение через \
                                 него.\nЧтобы продолжить нажмите help', reply_markup=button)
    await call.answer()
