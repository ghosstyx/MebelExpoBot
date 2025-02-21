from aiogram import Router, Bot, types
from aiogram.filters import Command
from aiogram.types import Message
from states.register import RegisterState
from aiogram.fsm.context import FSMContext

start_router = Router()
@start_router.message(Command("start"))
async def start_command(message: Message,  state: FSMContext):
    await message.answer(
        f"Добро пожаловать! {message.from_user.full_name} 👋\n"
        "Я бот для регистрации посетителей стенда INFINITY на MebelExpo 2025.\n"
        "Зарегестрируйтесь и получите уникальную скидку в виде 25% на любые товары! \n"
        "Введите ваше имя и фамилию:"
    )
    await state.set_state(RegisterState.name)
