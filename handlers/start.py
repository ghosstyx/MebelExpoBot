from loader import dp
from aiogram.filters import Command
from aiogram import types


user_data = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    user_data[message.from_user.id] = {}
    await message.answer("Привет! Давай зарегистрируем тебя для получения 25% скидки.")
