import asyncio
from handlers import *
from loader import bot, dp
from utils.set_bot_commands import set_default_commands


async def main():
    await set_default_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("bot is active")
    asyncio.run(main())