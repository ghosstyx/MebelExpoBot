import asyncio
from loader import bot, dp
from handlers.register import register_router
from handlers.start import start_router
from utils.set_bot_commands import set_default_commands


# Подключаем роутеры
dp.include_router(start_router)
dp.include_router(register_router)


async def main():
    await set_default_commands(bot)

    async with bot:
        print("Bot is active")
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
