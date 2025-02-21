from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message

from loader import bot
import re
from aiogram.fsm.context import FSMContext
from states.register import RegisterState
from google_sheets import add_visitor_data, is_phone_registered
from keyboards.contact import contact_keyboard

register_router = Router()


def is_valid_name(name):
    return bool(re.fullmatch(r"[А-Яа-яA-Za-z\s-]{2,}", name))


def is_valid_date(date_text):
    return bool(re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", date_text))


def is_valid_phone(phone):
    return bool(re.fullmatch(r"\+\d{10,15}", phone))


# 📌 1. Сохраняем имя и запрашиваем дату рождения
@register_router.message(RegisterState.name)
async def process_name(message: Message, state: FSMContext):
    if not is_valid_name(message.text):
        await message.answer("Некорректное имя! Введите имя, используя только буквы и пробелы (например, Иван Иванов).")
        return

    await state.update_data(name=message.text)
    await message.answer("📅 Отлично! Теперь введите вашу дату рождения (в формате ДД.ММ.ГГГГ):")
    await state.set_state(RegisterState.birthdate)


# 📌 2. Сохраняем дату рождения и запрашиваем номер телефона
@register_router.message(RegisterState.birthdate)
async def process_birthdate(message: Message, state: FSMContext):
    if not is_valid_date(message.text):
        await message.answer("Неверный формат! Введите дату рождения в формате ДД.ММ.ГГГГ (например, 11.11.2000).")
        return

    await state.update_data(birthdate=message.text)
    await message.answer("📞 Почти готово! Отправьте свой контактный номер телефона (используйте кнопку ниже 👇).", reply_markup=contact_keyboard)
    await state.set_state(RegisterState.phone)


# 📌 4. Сохраняем номер телефона и запрашиваем селфи
@register_router.message(RegisterState.phone, F.contact)
async def process_phone(message: Message, state: FSMContext):
    if not message.contact:
        await message.answer("Пожалуйста, отправьте ваш контакт через кнопку.")
        return
    phone = message.contact.phone_number
    if not is_valid_phone(phone):
        await message.answer("Неверный формат! Попробуйте еще раз.")
        return

    if is_phone_registered(phone):
        await message.answer("Ошибка: Аккаунт с этим номером уже существует! 🚫")
        return

    await state.update_data(phone=message.contact.phone_number)
    await message.answer("📸 Финальный шаг! Прикрепите селфи на фоне нашего стенда, чтобы подтвердить своё участие.")
    await state.set_state(RegisterState.photo)


# 📌 5. Завершаем регистрацию и отправляем данные в Google Sheets
@register_router.message(RegisterState.photo, F.photo)
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = message.from_user.id
    full_name = data["name"]
    birth_date = data["birthdate"]
    phone = data["phone"]

    photo_id = message.photo[-1].file_id
    date = message.date.strftime("%d.%m.%Y")

    file = await bot.get_file(photo_id)
    photo_url = f"https://api.telegram.org/file/bot{bot.token}/{file.file_path}"
    try:
     add_visitor_data(user_id, full_name, birth_date, phone, photo_url, date)
    except ValueError as e:
        await message.answer(str(e))
    except Exception as e:
        await message.answer(f"Ошибка при регистрации: {e}")
    await message.answer(f"""
✅ Регистрация завершена!

🎉 Вам присвоен уникальный номер: #{message.from_user.id}

📌 Теперь вы можете воспользоваться скидкой 25%:
🔹 Прямо на выставке (оформите накладную у менеджера).
🔹 В наших шоурумах на Джами (https://yandex.uz/maps/-/CHuJQB8C) или Чинабаде (https://yandex.uz/maps/-/CHuJQU72) в течение трёх дней.

📅 Срок действия скидки: с 25 по 27 февраля 2025 года.
📢 Скидка не ограничена по количеству покупок!

Спасибо за участие! Ждём вас за выгодными покупками. 🏆
https://yandex.uz/maps/-/CHuJQB8C
""")
    await state.clear()