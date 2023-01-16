from aiogram import types
from aiogram.types import CallbackQuery
from googletrans import Translator
from loader import dp, bot

tarjimon = Translator()
# Echo bot
# @dp.message_handler()
# async def bot_echo(message: types.Message):
#     til = tarjimon.detect(text=message.text).lang
#     await message.reply(text=f"Ushbu text {til} tilida yozilgan")

@dp.callback_query_handler(text='uzru')
async def bot_echo(message : CallbackQuery):
    await bot.send_message(chat_id=message.from_user.id,text=f"Salom - Hello ! \n\n🇺🇿Tarjima qilmoqchi bo'lgan habaringizni yuboring \n🇷🇺Отправьте сообщение, которое хотите перевести")

@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang
    try:
     if til=='uz':
         matn = tarjimon.translate(text=message.text,dest='ru',src='uz')
         await message.reply(text=matn.text)

     elif til=='uz':
         en = tarjimon.translate(text=message.text,dest='uz',src='ru')
         await message.reply(text=en.text)
    except:
        await message.answer("Bunday so'z topilmadi❌")


