from flask import request
from flask import jsonify
from flask_restx import Resource
from app.main.dto.telegram import TelegramDTO

from app.main.service.telegram import TelegramService
from app.main.service.athena import AthenaService


api = TelegramDTO.api
res = TelegramDTO.response


@api.route('/<string:username>/')
@api.param('username', 'The channel username identifier')
class TelegramMessages(Resource):
    @api.response(200, 'Messages returned successfully.', res)
    @api.doc('fetch telegram channel posts based on username',
             params={'offset_id': {
                 'description': 'offset_id for pagination',
                 'in': 'query',
                 'type': 'int'
             }})
    def get(self, username):
        offset_id = int(request.args.get('offset_id', 0))

        service = TelegramService()
        messages = service.get_messages(username=username, offset_id=offset_id)

        text_list = [msg['text'] if msg['text'] is not None else '' for msg in messages]
        athena_service = AthenaService()
        sentiment = athena_service.get_predicted_sentiment(text_list)
        for index, msg in enumerate(messages):
            msg['sentiment'] = sentiment[index]

        res = {
            'messages': messages
        }

        return jsonify(res)
