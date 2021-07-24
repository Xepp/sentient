from pyrogram import Client


class TelegramAdapter:

    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash

    def initialize(self):
        with Client('client', self.api_id, self.api_hash) as app:
            app.send_message('me', 'sentient')

    @staticmethod
    def parse_message(message):
        return {
            'id': message.message_id,
            'date': message.date,
            'text': message.caption if message.media else message.text,
            'views': message.views,
            'link': message.link,
            'channel': {
                'username': message.chat.username,
                'title': message.chat.title
            }
        }

    def get_channel_messages(self, username, offset_id=0):
        with Client('client', self.api_id, self.api_hash, no_updates=True) as app:
            messages = app.get_history(username, offset_id=offset_id)

            return [self.parse_message(message) for message in messages]
