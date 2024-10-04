from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters import CommandStart
import os
from database.sq_db import select_ncs_page, select_by_pages
from config import TOKEN


dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: types.Message):
    """Хендлер на команду /start."""
    await message.reply("Введите код цвета NCS.\nНапример, для NCS S 0502-Y50R\nвведите 0502-Y50R")
    await message.delete()

# @dp.message(lambda x: 0 < int(x) < 217)
# async def echo_message(message: types.Message):
#     text = message.text.upper()
#     try:
#         page = select_by_pages(text)
#         await message.reply_photo(
#             photo=types.FSInputFile(os.path.join('colors', f'{text}.jpg')),
#             caption=page,
#         )
#     except Exception as ex:
#         await message.reply(
#             text='Некорректный код цвета',
#         )


@dp.message()
async def echo_message(message: types.Message):
    text = message.text.upper()

    try:
        ncs_page = select_ncs_page(text)
        await message.reply_photo(
            photo=types.FSInputFile(os.path.join('colors', f'{text}.jpg')),
            caption='    '.join(ncs_page),
        )

    except Exception as ex:
        await message.reply(
            text='Некорректный код цвета',
        )
    
    await message.delete()


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


asyncio.run(main())
