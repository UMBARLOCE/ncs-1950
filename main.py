import asyncio

import handler
from keyboard.menu import set_menu
from middleware import CheckSubscriptionMiddleware
from utils.config import main_channel_name
from utils.loader import dp, bot


async def main() -> None:
    dp.startup.register(set_menu)

    dp.include_router(handler.callback.router)
    dp.include_router(handler.command.router)
    dp.include_router(handler.message.router)

    dp.message.middleware(CheckSubscriptionMiddleware(main_channel_name))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
