from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uz🇺🇿 👉 Ru🇷🇺',callback_data='uzru')
        ],
        [
            InlineKeyboardButton(text='Uz🇺🇿 👉 Eng🇬🇧',url='https://t.me/UzEn_TranslaterBot')
        ],
        [
            InlineKeyboardButton(text="Uz🇺🇿 👉Arab🇸🇦",url='https://t.me/UzArab_TranslaterBot')
        ]
    ]
)