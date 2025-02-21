from aiogram import Bot, types


async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Запустить бота"),
    ])