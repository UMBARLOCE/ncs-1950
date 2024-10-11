from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_ikb_examples_ncs(ncs: str) -> InlineKeyboardMarkup:
    """Возвращает клавиатуру с сайтами по заданному цвету NCS.
    
    На сайтах имеются картинки интерьера с заданным цветом NCS.
    """
    ncs_ = ncs.replace('-', '_')
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Пример 1",
                    url=f'https://akkras.ru/colors/ncs_index_original/ncs_s_{ncs_.lower()}.html'),

                InlineKeyboardButton(
                    text="Пример 2",
                    url=f'https://www.market-krasok.ru/help/colors/ncs_second_edition/S-{ncs.upper()}/'),
            ],
        ]
    )
    return keyboard
