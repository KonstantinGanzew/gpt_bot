import logging
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from api_openai import *
import keyboards.inline.choice_buttons as key
import keyboards.inline.callback_datas as call_datas
from bd.sqlite import *

# Обработчик команды start
async def show_menu(message: Message):
    logging.info(f'msg = "{message.chat.id}, {message.from_user.username}, {message.text}')
    await bot.send_message(chat_id=message.chat.id, 
                           text='Привет, я тот кто способен помочь тебе...\nВсего пару уточнений.', 
                           reply_markup=key.menu_keyboard)

# Вывод или добавление нового значения для пробега
async def mileages(user_id, message):
    if ' ' in message:
        await set_mileage(user_id, message.split(' ')[1])
        mileages = message.split(' ')[1]
    else:
        mileages = (await get_mileage(user_id))[0][0]
    await bot.send_message(chat_id=user_id, text=f'Последняя замена масла была: {mileages}')

async def content(user_id, message):
    previous = await bot.send_message(chat_id=user_id, text='Нейросеть генерирует ответ')
    history = json.loads((await get_message(user_id))[0][0])
    history.append({'role': 'user','content': message})
    contents = await get_messages_list(history)
    await bot.edit_message_text(chat_id=user_id, message_id=previous.message_id,
                           text=contents[-1]['content'],
                           reply_markup=key.clear_message)
    await set_message(user_id, json.dumps(contents))

async def help(user_id):
    await bot.send_message(chat_id=user_id, text='Список команд:\
                           \n/start активировать бота\
                           \n/help ввывод список команд\
                           \n/balance покажет текущий баланс\
                           \n/mileage без параметров покажет пробег в который осуществлялось замена масла, если он был проставлен заранее. /mileage число задаст новый параметр\
                           \nНапишите любой интересующий вас вопрос, бот постарается ответить, если вас больше не интересует данная тема нажмите "Закончить тему"')

# Первый пункт    
@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu='next'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Я бот OpenAi,\nсоздан @kureed для облегчения жизни, так как всякие ресурсы OpenAi либо имеют бешаные цены, либо работают 1 день, было решено взять свой токен и попробовать общение через него.\nЧтобы продолжить напишите любой вопрос.')
    await call.answer()

@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu='communication'))
async def communication(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Для общения с ботом, напишите сообщение, я постараюсь ответить')
    await call.answer()

@dp.callback_query_handler(call_datas.clear_callback.filter(item_clear='clear'))
async def clear_field(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text(call.message.text) 
    await set_message(call.from_user.id, '[]')
    await call.answer(text='Запрос сброшен', show_alert=False)

# Тестовый вариант обращения к чат гпт и прочим штукам, в дальнейшем все предположительно будет проходить тут
@dp.message_handler(content_types=['text'])
async def echo(message: Message):
    logging.info(f'msg = "{message.chat.id}, {message.from_user.username}, {message.text}')
    if  message.text == '/start':
        await create_profile(message.chat.id)
        await show_menu(message)
    elif message.text == '/help':
        await help(message.chat.id)
    elif message.text == '/balance':
        await bot.send_message(chat_id=message.chat.id, text=f'Баланс на счете {await balance()}')
    elif '/mileage' in message.text:
        await mileages(message.chat.id, message.text)
    else:
        await content(message.chat.id, message.text)
