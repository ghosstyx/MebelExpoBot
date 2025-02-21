import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

GOOGLE_SHEET_ID = "ВАШ ТОКЕН"
sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

sheet.append_row(["Test", "123", "example@gmail.com"])

print("✅ Данные успешно добавлены в Google Таблицу!")

print(os.path.exists("credentials.json"))