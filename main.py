from aiogram import types
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook
import asyncio
import os
from database.sq_db import (
    select_ncs_code_and_page_number_by_ncs_code,
    select_ncs_codes_by_page_number,
)
from loader import dp, bot
from config import main_channel_name
from middleware import CheckSubscriptionMiddleware


@dp.message(CommandStart())
async def start_command(message: types.Message) -> None:
    """Хендлер на команду /start."""

    try:
        await message.answer(
            "Введите код цвета без приставки NCS S (например 0570-Y80R)\n"
            "или\n"
            "введите номер страницы веера NCS index 1950 с 1 по 216"
        )

    except Exception:
        await message.answer('Неверный формат запроса')
    
    finally:
        await message.delete()


@dp.message(lambda message: message.text.isdigit() and 0 < int(message.text) < 217)
async def find_colors_by_page_number(message: types.Message) -> None:
    """Хендлер на номер страницы веера."""
    page_number: str = message.text

    try:
        colors: list[str] = select_ncs_codes_by_page_number(page_number)
        for color in colors:
            await message.reply_photo(
                photo=types.FSInputFile(os.path.join('colors', f'{color}.jpg')),
                caption='    '.join((color, page_number)),
                disable_notification=True,
            )

    except Exception:
        await message.answer('Неверный формат запроса')
    
    finally:
        await message.delete()


@dp.message()
async def find_color_by_ncs_code(message: types.Message) -> None:
    """Хендлер на код цвета."""
    ncs_code: str = message.text.upper()

    try:
        ncs_page = select_ncs_code_and_page_number_by_ncs_code(ncs_code)
        await message.reply_photo(
            photo=types.FSInputFile(os.path.join('colors', f'{ncs_code}.jpg')),
            caption='    '.join(ncs_page),
            disable_notification=True,
        )

    except Exception:
        await message.answer('Неверный формат запроса')
    
    finally:
        await message.delete()


async def main() -> None:
    dp.message.middleware(CheckSubscriptionMiddleware(main_channel_name))
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
