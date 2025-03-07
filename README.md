# Telegram Bot for MebelExpo 2025

## Описание
Этот бот предназначен для регистрации посетителей стенда INFINITY на выставке MebelExpo 2025. 

## Запуск бота
1. Убедитесь, что у вас установлен Python 3.9+.
2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
3. Создайте файл `.env` и укажите в нем свои токены и API-ключи.
4. Запустите бота с помощью команды:
   ```sh
   python runbot.py
   ```

## Тестирование соединения с Google Sheets
Для проверки подключения к Google Sheets используйте скрипт `test_google.py`:
```sh
python test_google.py
```

## Конфигурация
1. **.env файл**: 
   - Создайте `.env` в корне проекта.
   - Укажите там API-ключи, токены и идентификатор Google Sheets.

2. **Google Sheets API**:
   - Создайте сервисный аккаунт в Google Cloud.
   - Скачайте JSON-ключ и укажите путь к нему в `.env`.

3. **Credentials.json:**
   - Импортируйте json файл с google cloud console для связи с таблицей