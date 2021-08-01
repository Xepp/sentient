from flask_restx import Namespace
from flask_restx import fields


class InstagramDTO:
    api = Namespace('instagram', description='instagram related operations')
    comment = api.model('InstagramComment', {
        'id': fields.String,
        'text': fields.String,
        'created_at': fields.DateTime,
        'username': fields.String,
        'sentiment': fields.String
    })
    response = api.model('InstagramResponse', {
        'comments': fields.List(fields.Nested(comment)),
        'has_next_page': fields.Boolean,
        'new_end_cursor': fields.String
    })
