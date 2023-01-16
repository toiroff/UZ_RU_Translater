from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.menyu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom,Всем привет ! {message.from_user.full_name}!",reply_markup=menu)
