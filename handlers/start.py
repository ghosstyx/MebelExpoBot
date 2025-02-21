from aiogram import Router, Bot, types
from aiogram.filters import Command
from aiogram.types import Message
from states.register import RegisterState
from aiogram.fsm.context import FSMContext

WELCOME_TXT = """
👋 Добро пожаловать на стенд INFINITY на MebelExpo 2025!

🎉 Только для посетителей выставки — эксклюзивная скидка 25% на ассортимент INFINITY в течение трёх дней!

📌 Как получить скидку?
1️⃣ Пройдите быструю регистрацию.
2️⃣ Прикрепите селфи с нашим стендом.
3️⃣ После регистрации получите уникальный номер и возможность воспользоваться скидкой на месте или в шоурумах (Джами, Чинабад) в течение 3 дней.

📩 Давайте начнём!

➡️ Введите ваше имя и фамилию:
"""

start_router = Router()
@start_router.message(Command("start"))
async def start_command(message: Message,  state: FSMContext):
    await message.answer(WELCOME_TXT)
    await state.set_state(RegisterState.name)
