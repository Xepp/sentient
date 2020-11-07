from flask import Blueprint
from flask import request
from flask import jsonify

from app.main.service.telegram import TelegramService
from app.main.service.athena import AthenaService


telegram_blueprint = Blueprint('telegram', __name__)


@telegram_blueprint.route('/<string:username>/', methods=['GET'])
def get_messages_by_username(username):
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

