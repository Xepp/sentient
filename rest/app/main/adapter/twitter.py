import tweepy

from app.main.util.helper import tweet_cleanizer


class TwitterAdapter:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def get_user_timeline(self, screen_name, since_id=None, max_id=None, count=50):
        timeline = self.api.user_timeline(
            screen_name=screen_name,
            since_id=since_id,
            max_id=max_id,
            count=count,
            tweet_mode='extended')

        return [tweet_cleanizer(tweet) for tweet in timeline]
