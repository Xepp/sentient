from flask import request
from flask import jsonify
from flask_restx import Resource
from app.main.dto.twitter import TwitterDTO

from app.main.service.twitter import TwitterService
from app.main.service.athena import AthenaService


api = TwitterDTO.api
res = TwitterDTO.response


@api.route('/<string:username>/')
@api.param('username', 'The Account username identifier')
class TwitterTweets(Resource):
    @api.response(200, 'Tweets returned successfully.', res)
    @api.doc('fetch instagram post comments based on shortcode',
             params={
                 'since_id': {
                     'description': 'since_id for pagination (get newer tweets than this id)',
                     'in': 'query',
                     'type': 'string'
                 },
                 'max_id': {
                     'description': 'max_id for pagination (get older tweets than this id)',
                     'in': 'query',
                     'type': 'string'
                 }
             })
    def get(self, username):
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
