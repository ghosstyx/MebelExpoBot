import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Подключаем credentials.json
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Открываем таблицу по ID
GOOGLE_SHEET_ID = "14qkAoJDt2o5yy4HvSr8f4kZ72krch3HEcvDWuWYJajE"
sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

# Добавляем тестовую строку
sheet.append_row(["Test", "123", "example@gmail.com"])

print("✅ Данные успешно добавлены в Google Таблицу!")

import os

print(os.path.exists("credentials.json"))