import os

from app.main.adapter.athena import AthenaAdapter


class AthenaService:

    def __init__(self):
        self.adapter = AthenaAdapter(base_url=os.getenv('ATHENA_BASE_URL'))

    def get_predicted_sentiment(self, text_list):
        predicted_sentiment = self.adapter.get_batch_sentiment(text_list=text_list)

        return predicted_sentiment['predicted']

