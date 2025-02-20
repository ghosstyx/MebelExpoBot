import gspread
from oauth2client.service_account import ServiceAccountCredentials

from config import GOOGLE_SHEET_ID

# Авторизация через Google API
def authorize_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client

# Получаем таблицу
def get_sheet():
    client = authorize_google_sheets()
    sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1  # Открываем первый лист
    return sheet

# Функция для добавления данных в таблицу
def add_visitor_data(user_id, name, birth_date, phone, photo_url):
    sheet = get_sheet()
    row = [user_id, name, birth_date, phone, photo_url, "Не использована"]
    sheet.append_row(row)  # Добавляем строку в таблицу
