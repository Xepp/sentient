from flask_restx import Namespace
from flask_restx import fields


class TelegramDTO:
    api = Namespace('telegram', description='telegram related operations')
    channel = api.model('TelegramMessageChannel', {
        'username': fields.String,
        'title': fields.String
    })
    message = api.model('TelegramMessage', {
        'id': fields.Integer,
        'date': fields.DateTime,
        'text': fields.String,
        'views': fields.Integer,
        'link': fields.Url,
        'channel': fields.Nested(channel),
        'sentiment': fields.String
    })
    response = api.model('TelegramResponse', {
        'messages': fields.List(fields.Nested(message))
    })
