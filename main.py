from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters import CommandStart
import os
from database.sq_db import select_ncs_page, select_by_pages
from config import TOKEN


dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: types.Message) -> None:
    """Хендлер на команду /start."""
    await message.reply(
        "Введите код цвета\n"
        "без приставки NCS S\n"
        "или\n"
        "Введите номер страницы\n"
        "1 - 216"
    )
    await message.delete()


@dp.message(lambda message: message.text.isdigit() and 0 < int(message.text) < 217)
async def process_page(message: types.Message) -> None:
    """Хендлер на номер страницы веера."""
    page = message.text

    try:
        colors: list[str] = select_by_pages(page)
        for color in colors:
            await message.reply_photo(
                photo=types.FSInputFile(os.path.join('colors', f'{color}.jpg')),
                caption='    '.join((color, page)),
                disable_notification=True,
            )

    except Exception:
        await message.reply(
            text='Некорректный код цвета',
        )
    
    finally:
        await message.delete()


@dp.message()
async def process_ncs(message: types.Message) -> None:
    """Хендлер на код цвета."""
    text = message.text.upper()

    try:
        ncs_page = select_ncs_page(text)
        await message.reply_photo(
            photo=types.FSInputFile(os.path.join('colors', f'{text}.jpg')),
            caption='    '.join(ncs_page),
            disable_notification=True,
        )

    except Exception:
        await message.reply(
            text='Некорректный код цвета',
        )
    
    finally:
        await message.delete()


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
