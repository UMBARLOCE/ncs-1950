import asyncio
import os

from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook

from database import select_ncs_and_pages_by_ncs, select_ncs_and_pages_by_page
from filter import is_number_from_1_to_216
from keyboard.inline import get_ikb_examples_ncs
from middleware import CheckSubscriptionMiddleware
from utils.config import main_channel_name
from utils.loader import dp, bot


@dp.message(CommandStart())
async def message_start_command(message: types.Message) -> None:
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
async def callback_already_subscribed(callback: types.CallbackQuery) -> None:
    """Хендлер на подтверждение подписки на канал."""

    await callback.message.answer(
        "Введите код цвета без приставки NCS S (например 0570-Y80R)\n"
        "или\n"
        "введите номер страницы веера NCS index 1950 с 1 по 216"
    )
    await callback.answer()


@dp.callback_query(F.data.startswith('ncs_'))
async def callback_answer_by_ncs(callback: types.CallbackQuery) -> None:
    """Коллбек-Хендлер на код цвета."""
    ncs, pages = select_ncs_and_pages_by_ncs(callback.data.upper()[4:])
    await callback.message.reply_photo(
            photo=types.FSInputFile(os.path.join('colors', f'{ncs}.jpg')),
            caption='    '.join((ncs, pages)),
            disable_notification=True,
            reply_markup=get_ikb_examples_ncs(ncs),
            allow_sending_without_reply=False,
    )
    await callback.answer()
    # await asyncio.sleep(2)
    # await callback.message.delete()


@dp.callback_query(F.data == 'bad')
async def callback_answer_bad_push(callback: types.CallbackQuery) -> None:
    """Коллбек-Хендлер на кривое нажатие в инлайн-клавиатуре."""
    await callback.answer("Сюда не жми")


@dp.message(is_number_from_1_to_216)
async def message_answer_ncs_and_pages_by_page(message: types.Message) -> None:
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
        await message.answer('кривая страница')
    
    finally:
        await message.delete()


@dp.message()
async def message_answer_ncs_and_pages_by_ncs(message: types.Message) -> None:
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
        # await message.answer('пустой хендлер')
        answer = await message.answer('кривой код')
        await asyncio.sleep(2)
        await answer.delete()
    
    finally:
        await message.delete()


async def main() -> None:
    dp.message.middleware(CheckSubscriptionMiddleware(main_channel_name))
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
