from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import select_ncs_whiteness, select_ncs_chromaticness, select_ncs_hue


def get_ikb_examples_ncs(ncs: str) -> InlineKeyboardMarkup:
    """Возвращает клавиатуру с сайтами по заданному цвету NCS.
    
    На сайтах имеются картинки интерьера с заданным цветом NCS.
    """
    ncs_ = ncs.replace('-', '_')
    left_whiteness, right_whiteness = select_ncs_whiteness(ncs)
    left_chromaticness, right_chromaticness = select_ncs_chromaticness(ncs)
    left_hue, right_hue = select_ncs_hue(ncs)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            # [
            #     InlineKeyboardButton(
            #         text="Пример 1",
            #         url=f"https://akkras.ru/colors/ncs_index_original/ncs_s_{ncs_.lower()}.html",
            #     ),

            #     InlineKeyboardButton(
            #         text="Пример 2",
            #         url=f'https://www.market-krasok.ru/help/colors/ncs_second_edition/S-{ncs.upper()}/',
            #     ),
            # ],

            [
                InlineKeyboardButton(
                    text=left_whiteness if left_whiteness else '❌',
                    callback_data=f'ncs_{left_whiteness}' if left_whiteness else 'bad',
                ),

                InlineKeyboardButton(
                    text="тон",
                    callback_data='bad',
                ),

                InlineKeyboardButton(
                    text=right_whiteness if right_whiteness else '❌',
                    callback_data=f'ncs_{right_whiteness}' if right_whiteness else 'bad',
                ),
            ],

            [
                InlineKeyboardButton(
                    text=left_chromaticness if left_chromaticness else '❌',
                    callback_data=f'ncs_{left_chromaticness}' if left_chromaticness else 'bad',
                ),

                InlineKeyboardButton(
                    text="цветность",
                    callback_data='bad',
                ),

                InlineKeyboardButton(
                    text=right_chromaticness if right_chromaticness else '❌',
                    callback_data=f'ncs_{right_chromaticness}' if right_chromaticness else 'bad',
                ),
            ],

            [
                InlineKeyboardButton(
                    text=left_hue if left_hue else '❌',
                    callback_data=f'ncs_{left_hue}' if left_hue else 'bad',
                ),

                InlineKeyboardButton(
                    text="оттенок",
                    callback_data='bad',
                ),

                InlineKeyboardButton(
                    text=right_hue if right_hue else '❌',
                    callback_data=f'ncs_{right_hue}' if right_hue else 'bad',
                ),
            ],
        ]
    )
    return keyboard
