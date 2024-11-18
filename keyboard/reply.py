from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lex import color_code


def get_rkb_selection() -> ReplyKeyboardMarkup:
    buttons = [
        [
            KeyboardButton(text=color_code['жёлтый']),
            KeyboardButton(text=color_code['оранжевый']),
            KeyboardButton(text=color_code['красный']),
        ],

        [
            KeyboardButton(text=color_code['салатовый']),
            KeyboardButton(text=color_code['бежевый']),
            KeyboardButton(text=color_code['фиолетовый']),
        ],

        [
            KeyboardButton(text=color_code['зелёный']),
            KeyboardButton(text=color_code['бирюзовый']),
            KeyboardButton(text=color_code['синий']),
        ],

    ]

    rkb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder='3030-R50B'
    )

    return rkb
