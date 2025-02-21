from aiogram import Router, Bot, types
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()  # Создаём роутер

@start_router.message(Command("start"))
async def start_command(message: Message, bot: Bot):
    await message.answer(
        "Привет! 👋\n"
        "Я бот для регистрации посетителей стенда INFINITY на MebelExpo 2025.\n"
        "Нажми /register, чтобы начать регистрацию."
    )
