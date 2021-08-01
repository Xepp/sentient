from flask_restx import Namespace
from flask_restx import fields


class TwitterDTO:
    api = Namespace('twitter', description='twitter related operations')
    user = api.model('TwitterUser', {
        'id': fields.String,
        'name': fields.String,
        'screen_name': fields.String,
        'description': fields.String,
        'followers_count': fields.Integer,
        'followings_count': fields.Integer,
        'statuses_count': fields.Integer,
        'avatar': fields.Url
    })
    tweet = api.model('TwitterTweet', {
        'id': fields.String,
        'created_at': fields.DateTime,
        'text': fields.String,
        'type': fields.String,
        'retweet_count': fields.Integer,
        'favorite_count': fields.Integer,
        'channel': fields.Nested(user),
        'sentiment': fields.String
    })
    response = api.model('TwitterResponse', {
        'tweets': fields.List(fields.Nested(tweet))
    })
