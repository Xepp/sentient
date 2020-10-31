def get_tweet_type(tweet):
    if 'retweeted_status' in tweet:
        return 'retweet'
    elif 'quoted_status' in tweet:
        return 'quote'
    elif tweet.get('in_reply_to_status_id') is not None:
        return 'reply'

    return 'tweet'


def tweet_cleanizer(status):
    tweet = getattr(status, '_json')
    tweet_type = get_tweet_type(tweet)
    text = tweet.get('extended_tweet', {}).get('full_text', tweet.get('text', ''))

    return {
        'id': tweet.get('id_str'),
        'created_at': tweet.get('created_at'),
        'text': text,
        'type': tweet_type,
        'user': {
            'id': tweet.get('user', {}).get('id_str'),
            'name': tweet.get('user', {}).get('name'),
            'screen_name': tweet.get('user', {}).get('screen_name'),
            'description': tweet.get('user', {}).get('description'),
            'followers_count': tweet.get('user', {}).get('followers_count'),
            'followings_count': tweet.get('user', {}).get('friends_count'),
            'statuses_count': tweet.get('user', {}).get('statuses_count'),
            'avatar': tweet.get('user', {}).get('profile_image_url')
        },
        'retweet_count': tweet.get('retweet_count'),
        'favorite_count': tweet.get('favorite_count')
    }

