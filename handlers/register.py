from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from states.register import Registration  # Импортируем состояния из states/register.py
from google_sheets import add_visitor_data  # Функция для Google Sheets

# Создаем роутер
router = Router()

# Запуск регистрации
@router.message(F.text.lower() == "/start")
async def start_registration(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("Привет! Введи свое *Имя и Фамилию*.", parse_mode="Markdown")

# Получение имени
@router.message(Registration.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.birthdate)
    await message.answer("Теперь введи дату рождения *ДД.ММ.ГГГГ*.", parse_mode="Markdown")

# Получение даты рождения
@router.message(Registration.birthdate)
async def get_birthdate(message: Message, state: FSMContext):
    await state.update_data(birthdate=message.text)
    await state.set_state(Registration.phone)
    await message.answer("Отправь номер телефона.", reply_markup=contact_keyboard)

# Получение телефона
@router.message(F.contact, Registration.phone)
async def get_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(Registration.photo)
    await message.answer("Теперь отправь *селфи* на фоне стенда.", parse_mode="Markdown")

# Получение фото
@router.message(F.photo, Registration.photo)
async def get_photo(message: Message, state: FSMContext):
    user_data = await state.get_data()
    add_visitor_data(user_data["name"], user_data["birthdate"], user_data["phone"], "photo_url")  # Заглушка для фото

    await message.answer("✅ Регистрация завершена! Твоя скидка активирована!")
    await state.clear()  # Завершаем FSM


