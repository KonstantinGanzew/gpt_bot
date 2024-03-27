from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import keyboards.inline.callback_datas as key

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Давай дальше', callback_data=key.menu_callback.new(item_menu='next')),
        ],
        [
            InlineKeyboardButton(text='Я уже все знаю, давай общаться', callback_data=key.menu_callback.new(item_menu='communication')),
        ],
    ]
)