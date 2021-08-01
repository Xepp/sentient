from flask_restx import Namespace
from flask_restx import fields


class WebDTO:
    api = Namespace('web', description='web related operations')
    comment = api.model('KhabarFooriComment', {
        'author': fields.String,
        'date': fields.DateTime,
        'text': fields.String,
        'pos': fields.Integer,
        'neg': fields.Integer,
        'sentiment': fields.String
    })
    comment_with_replays = api.inherit('KhabarFooriCommentWithReplays', comment, {
        'replays': fields.List(fields.Nested(comment))
    })
    response = api.model('KhabarFooriResponse', {
        'comments': fields.List(fields.Nested(comment_with_replays))
    })
