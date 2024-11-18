from aiogram import types, Router
from aiogram.filters import CommandStart, Command

from keyboard.reply import get_rkb_selection


router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message) -> None:
    """Хендлер на команду /start."""

    try:
        await message.answer(
            "Введите код цвета без приставки NCS S (например 2030-R20B)\n"
            "или\n"
            "введите номер страницы веера NCS index 1950 с 1 по 216\n"
            "или\n"
            "выберите оттенок в цветовом кольце.",
            reply_markup=get_rkb_selection(),
            disable_notification=True,
        )

    except Exception:
        await message.answer('Неверный формат запроса')

    finally:
        await message.delete()


@router.message(Command('index_1950'))
async def command_index_1950(message: types.Message) -> None:
    """Хендлер на команду /index_1950."""

    try:
        await message.answer(
            "Введите код цвета без приставки NCS S (например 2030-R20B)\n"
            "или\n"
            "введите номер страницы веера NCS index 1950 с 1 по 216",
            disable_notification=True,
        )

    except Exception:
        await message.answer('Неверный формат запроса')

    finally:
        await message.delete()


@router.message(Command('selection'))
async def command_selection(message: types.Message) -> None:
    """Хендлер на команду /selection."""

    try:
        await message.answer(
            text="Выберите основной оттенок",
            reply_markup=get_rkb_selection(),
            disable_notification=True,
            )

    except Exception:
        await message.answer('Неверный формат запроса')

    finally:
        await message.delete()


@router.message(Command('about'))
async def command_about(message: types.Message) -> None:
    """Хендлер на команду /about."""

    try:
        await message.answer(
            text="https://materiale.ru/1490",
            disable_notification=True,
            )

    except Exception:
        await message.answer('Неверный формат запроса')
    
    finally:
        await message.delete()


@router.message(Command('help'))
async def command_help(message: types.Message) -> None:
    """Хендлер на команду /help."""

    try:
        await message.answer(
            text="Тут текст ОПИСАНИЕ",
            # reply_markup=types.ReplyKeyboardRemove(),
            disable_notification=True,
            )

    except Exception:
        await message.answer('Неверный формат запроса')
    
    finally:
        await message.delete()
