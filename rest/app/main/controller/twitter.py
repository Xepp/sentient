from flask import Blueprint
from flask import request
from flask import jsonify

from app.main.service.twitter import TwitterService
from app.main.service.athena import AthenaService


twitter_blueprint = Blueprint('twitter', __name__)


@twitter_blueprint.route('/<string:username>/', methods=['GET'])
def get_tweets_by_username(username):
    since_id = request.args.get('since_id', None)
    max_id = request.args.get('max_id', None)

    service = TwitterService()
    tweets = service.get_timeline(user=username, since_id=since_id, max_id=max_id)

    text_list = [tweet['text'] for tweet in tweets]
    athena_service = AthenaService()
    sentiment = athena_service.get_predicted_sentiment(text_list)
    for index, tweet in enumerate(tweets):
        tweet['sentiment'] = sentiment[index]

    res = {
        'tweets': tweets
    }

    return jsonify(res)

