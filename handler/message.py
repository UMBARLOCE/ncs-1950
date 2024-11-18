import asyncio
import os

from aiogram import types, Router, F

from database import select_ncs_and_pages_by_ncs, select_ncs_and_pages_by_page
from filter import is_number_from_1_to_216
from keyboard.inline import get_ikb_examples_ncs
from lexicon.lex import color_code


router = Router()

@router.message(is_number_from_1_to_216)
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


@router.message(F.text.in_(color_code.values()))
async def message_answer_to_hue(message: types.Message) -> None:
    """Хендлер на оттенок цвета."""

    try:
        hue = message.text.split()

        if hue[1] == 'N':
            color = '5000-N'

        elif len(hue) == 2:
            color = f'3030-{hue[1]}'

        elif len(hue) == 3:
            color = f'3030-{hue[0]}50{hue[2]}'

        ncs, pages = select_ncs_and_pages_by_ncs(color)
        await message.reply_photo(
            photo=types.FSInputFile(os.path.join('colors', f'{ncs}.jpg')),
            caption='    '.join((ncs, pages)),
            disable_notification=True,
            reply_markup=get_ikb_examples_ncs(ncs),
        )

    except Exception:
        answer = await message.answer('Неверный формат запроса')
        await asyncio.sleep(2)
        await answer.delete()
    
    finally:
        await message.delete()


@router.message()
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
        answer = await message.answer('Неверный формат запроса')
        await asyncio.sleep(2)
        await answer.delete()
    
    finally:
        await message.delete()
