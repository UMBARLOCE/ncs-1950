from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import select_ncs_whiteness


def get_ikb_examples_ncs(ncs: str) -> InlineKeyboardMarkup:
    """Возвращает клавиатуру с сайтами по заданному цвету NCS.
    
    На сайтах имеются картинки интерьера с заданным цветом NCS.
    """
    left, right = select_ncs_whiteness(ncs)
    ncs_ = ncs.replace('-', '_')
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="Пример 1",
                    url=f"https://akkras.ru/colors/ncs_index_original/ncs_s_{ncs_.lower()}.html",
                ),

                InlineKeyboardButton(
                    text="Пример 2",
                    url=f'https://www.market-krasok.ru/help/colors/ncs_second_edition/S-{ncs.upper()}/',
                ),
            ],

            [
                InlineKeyboardButton(
                    text=left if left else '❌',
                    callback_data=f'ncs_{left}' if left else 'bad',
                ),

                InlineKeyboardButton(
                    text="ТОН",
                    callback_data='bad',
                ),

                InlineKeyboardButton(
                    text=right if right else '❌',
                    callback_data=f'ncs_{right}' if right else 'bad',
                ),
            ],
        ]
    )
    return keyboard
