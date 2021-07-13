import os

from app.main.adapter.telegram import TelegramAdapter


class TelegramService:

    def __init__(self):
        self.adapter = TelegramAdapter(
            api_id=os.getenv('TELEGRAM_APP_API_ID'),
            api_hash=os.getenv('TELEGRAM_APP_API_HASH')
        )

    def get_messages(self, username, offset_id=0):
        messages = self.adapter.get_channel_messages(username=username, offset_id=offset_id)

        return messages

