import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEET_ID
import os


def authorize_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    if not os.path.exists("C:/Users/xulka/PycharmProjects/MebelExpoBot/credentials.json"):
        raise FileNotFoundError("Файл credentials.json не найден. Проверь путь к файлу.")

    creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/xulka/PycharmProjects/MebelExpoBot/credentials.json", scope)
    client = gspread.authorize(creds)
    return client

def get_sheet():
    try:
        client = authorize_google_sheets()
        sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1  # Открываем первый лист
        return sheet
    except gspread.exceptions.SpreadsheetNotFound:
        raise ValueError("Ошибка: Таблица не найдена. Проверь GOOGLE_SHEET_ID.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при получении таблицы: {e}")

def add_visitor_data(user_id, name, birth_date, phone, photo_url):
    sheet = get_sheet()
    row = [user_id, name, birth_date, phone, photo_url, "Не использована"]

    try:
        sheet.append_row(row)
        print("Данные успешно добавлены в Google Sheets.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при добавлении данных: {e}")

