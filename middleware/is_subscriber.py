from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Callable, Dict, Any, Awaitable


class CheckSubscriptionMiddleware(BaseMiddleware):
    """
    Этот middleware будет проверять подписку пользователя
    на указанный канал перед обработкой любого сообщения.
    Если пользователь не подписан, он получит сообщение
    с просьбой подписаться и кнопкой для перехода в канал.
    """

    def __init__(self, channel_name: str):
        self.channel_name = channel_name
        super().__init__()

    async def __call__(self,
                        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                        event: Message,
                        data: Dict[str, Any]
                        ) -> Any:

        chat_member = await event.bot.get_chat_member(f'@{self.channel_name}', event.from_user.id)
        if chat_member.status == 'left':
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Подписаться", url=f"https://t.me/{self.channel_name}")]
                ]
            )
            answer_text = """Чтобы пользоваться ботом, 
подпишитесь на наш канал - 
агрегатор новостей в мире декоративных материалов"""

            await event.answer(text=answer_text, reply_markup=keyboard)
        else:
            return await handler(event, data)
