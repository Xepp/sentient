import requests


class AthenaAdapter:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_batch_sentiment(self, text_list):
        url = f'{self.base_url}/'
        body = {
            'sentences': text_list
        }
        r = requests.post(url, json=body)

        return r.json()

