from aiogram import types, Bot


async def set_menu(bot: Bot):
    main_menu_commands = [

        # types.BotCommand(
        #     command='/start',
        #     description='начать'
        # ),

        types.BotCommand(
            command='/selection',
            description='выбор оттенка'
        ),

        types.BotCommand(
            command='/index_1950',
            description='веер'
        ),

        types.BotCommand(
            command='/about',
            description='о нас'
        ),

        types.BotCommand(
            command='/help',
            description='помощь'
        ),

    ]

    await bot.set_my_commands(main_menu_commands)
