import asyncio
import os

from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook

from database import select_ncs_and_pages_by_ncs, select_ncs_and_pages_by_page
from keyboard.inline import get_ikb_examples_ncs
from middleware import CheckSubscriptionMiddleware
from utils.loader import dp, bot
from utils.config import main_channel_name


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


@dp.callback_query(F.data == 'already_subscribed')
async def sub_data(callback: types.CallbackQuery) -> None:
    """Хендлер на команду /start."""

    await callback.message.answer(
        "Введите код цвета без приставки NCS S (например 0570-Y80R)\n"
        "или\n"
        "введите номер страницы веера NCS index 1950 с 1 по 216"
    )
    await callback.answer()


@dp.message(lambda message: message.text and message.text.isdigit() and 0 < int(message.text) < 217)
async def answer_ncs_and_pages_by_page(message: types.Message) -> None:
    """Хендлер на номер страницы веера."""

    try:
        list_of_ncs_pages = select_ncs_and_pages_by_page(message.text.upper())
        for ncs, pages in list_of_ncs_pages:
            await message.reply_photo(
                photo=types.FSInputFile(os.path.join('colors', f'{ncs}.jpg')),
                caption='    '.join((ncs, pages)),
                disable_notification=True,
                reply_markup=get_ikb_examples_ncs(ncs),
            )

    except Exception:
        await message.answer('Неверный формат запроса')
    
    finally:
        await message.delete()


@dp.message()
async def answer_ncs_and_pages_by_ncs(message: types.Message) -> None:
    """Хендлер на код цвета."""

    try:
        ncs, pages = select_ncs_and_pages_by_ncs(message.text.upper())
        await message.reply_photo(
            photo=types.FSInputFile(os.path.join('colors', f'{ncs}.jpg')),
            caption='    '.join((ncs, pages)),
            disable_notification=True,
            reply_markup=get_ikb_examples_ncs(ncs),
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
