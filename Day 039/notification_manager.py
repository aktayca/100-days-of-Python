import requests
import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


class NotificationManager:

    def send_telegram_message(self, message):
        """ This sends a notification with a deal to Telegram. """
        parameters = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
        }

        response = requests.post(url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=parameters)
        response.raise_for_status()
        data = response.json()
        return data