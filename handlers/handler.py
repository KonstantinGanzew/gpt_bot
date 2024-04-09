import logging
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from api_openai import *
import keyboards.inline.choice_buttons as key
import keyboards.inline.callback_datas as call_datas

# Обработчик команды start
async def show_menu(message: Message):
    await bot.send_message(chat_id=message.chat.id, 
                           text='Привет, я тот кто способен помочь тебе...\nВсего пару уточнений.', 
                           reply_markup=key.menu_keyboard)

# Первый пункт    
@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu='next'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Я бот OpenAi,\
                                 создан @kureed для облегчения жизни, так как всякие ресурсы OpenAi либо имеют бешаные\
                                 цены, либо работают 1 день, было решено взять свой токен и попробовать общение через \
                                 него.\nЧтобы продолжить нажмите help')
    await call.answer()

# Тестовый вариант обращения к чат гпт и прочим штукам, в дальнейшем все предположительно будет проходить тут
@dp.message_handler(content_types=['text'])
async def echo(message: Message):
    if  message.text == '/start':
        await show_menu(message)
    elif message.text == '/help':
        await bot.send_message(chat_id=message.chat.id, text='Тебе нужна помощь?')
    elif message.text == '/balance':
        await bot.send_message(chat_id=message.chat.id, text=f'Баланс на счете {await balance()}')
    else:
        a = [
                {
                    'role': 'user',
                    'content': message.text,
                }
        ]
        c = await get_messages_list(a)
        await bot.send_message(chat_id=message.chat.id, text=c[-1]['content'])