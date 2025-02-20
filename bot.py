# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from google_sheets import add_visitor_data
#
#
# # # Храним данные пользователей перед сохранением
# # user_data = {}
#
# # # Клавиатура для отправки контакта
# # contact_keyboard = ReplyKeyboardMarkup(
# #     keyboard=[[KeyboardButton(text="📞 Отправить контакт", request_contact=True)]],
# #     resize_keyboard=True
# # )
#
# # # Команда /start
# # @dp.message(Command("start"))
# # async def start(message: types.Message):
# #     user_data[message.from_user.id] = {}
# #     await message.answer("Привет! Давай зарегистрируем тебя для получения 25% скидки.\nВведи свое имя и фамилию:")
#
# # Получаем имя
# @dp.message()
# async def get_name(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_data:
#         return
#
#     user_data[user_id]["name"] = message.text
#     await message.answer("Теперь введи свою дату рождения (в формате DD.MM.YYYY):")
#
# # Получаем дату рождения
# @dp.message()
# async def get_birth_date(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_data:
#         return
#
#     user_data[user_id]["birth_date"] = message.text
#     await message.answer("Отправь свой номер телефона, нажав на кнопку ниже.", reply_markup=contact_keyboard)
#
# # Получаем номер телефона
# @dp.message()
# async def get_phone(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_data or not message.contact:
#         return
#
#     user_data[user_id]["phone"] = message.contact.phone_number
#     await message.answer("Отлично! Теперь отправь селфи с нашим стендом.")
#
# # Получаем фото
# @dp.message()
# async def get_photo(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_data or not message.photo:
#         return
#
#     # Получаем URL фото
#     photo_id = message.photo[-1].file_id
#     photo_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{photo_id}"
#
#     # Сохраняем данные
#     user_info = user_data[user_id]
#     add_visitor_data(user_id, user_info["name"], user_info["birth_date"], user_info["phone"], photo_url)
#
#     # Очищаем временные данные
#     del user_data[user_id]
#
#     await message.answer("Спасибо за регистрацию! Ваша скидка активна в течение 3 дней.")
#
# # Запуск бота
# async def main():
#     print("Бот запущен...")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
