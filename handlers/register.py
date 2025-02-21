from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message
from loader import bot
from aiogram.fsm.context import FSMContext
from states.register import RegisterState
from google_sheets import add_visitor_data, is_phone_registered
from keyboards.contact import contact_keyboard

register_router = Router()


# 📌 1. Сохраняем имя и запрашиваем дату рождения
@register_router.message(RegisterState.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите вашу дату рождения (в формате DD.MM.YYYY):")
    await state.set_state(RegisterState.birthdate)


# 📌 2. Сохраняем дату рождения и запрашиваем номер телефона
@register_router.message(RegisterState.birthdate)
async def process_birthdate(message: Message, state: FSMContext):
    await state.update_data(birthdate=message.text)
    await message.answer("Отправьте ваш номер телефона:", reply_markup=contact_keyboard)
    await state.set_state(RegisterState.phone)


# 📌 4. Сохраняем номер телефона и запрашиваем селфи
@register_router.message(RegisterState.phone, F.contact)
async def process_phone(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    if is_phone_registered(phone):
        await message.answer("Ошибка: Аккаунт с этим номером уже существует! 🚫")
        return
    await state.update_data(phone=message.contact.phone_number)
    await message.answer("Теперь отправьте фото с нашим стендом.")
    await state.set_state(RegisterState.photo)


# 📌 5. Завершаем регистрацию и отправляем данные в Google Sheets
@register_router.message(RegisterState.photo, F.photo)
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = message.from_user.id
    full_name = data["name"]
    birth_date = data["birthdate"]
    phone = data["phone"]
    date = datetime.now()

    photo_id = message.photo[-1].file_id

    file = await bot.get_file(photo_id)
    photo_url = f"https://api.telegram.org/file/bot{bot.token}/{file.file_path}"
    add_visitor_data(user_id, full_name, birth_date, phone, photo_url, date)
    await message.answer("✅ Вы успешно зарегистрированы! Ваши данные обрабатываются. Ожидайте подтвердждения!")
    await state.clear()