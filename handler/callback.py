import os

from aiogram import types, Router, F

from database import select_ncs_and_pages_by_ncs
from keyboard.inline import get_ikb_examples_ncs


router = Router()


@router.callback_query(F.data == 'already_subscribed')
async def callback_already_subscribed(callback: types.CallbackQuery) -> None:
    """Хендлер на подтверждение подписки на канал."""

    await callback.message.answer(
        "Введите код цвета без приставки NCS S (например 0570-Y80R)\n"
        "или\n"
        "введите номер страницы веера NCS index 1950 с 1 по 216"
    )
    await callback.answer()


@router.callback_query(F.data.startswith('ncs_'))
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


@router.callback_query(F.data == 'bad')
async def callback_answer_bad_push(callback: types.CallbackQuery) -> None:
    """Коллбек-Хендлер на кривое нажатие в инлайн-клавиатуре."""
    await callback.answer("Сюда не жми")
