import os

from app.main.adapter.twitter import TwitterAdapter


class TwitterService:

    def __init__(self):
        self.adapter = TwitterAdapter(
            consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
            consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))

    def get_timeline(self, user, since_id=None, max_id=None):
        tweets = self.adapter.get_user_timeline(screen_name=user, since_id=since_id, max_id=max_id)

        return tweets

