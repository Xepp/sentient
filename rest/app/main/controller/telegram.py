from flask import Blueprint
from flask import request
from flask import jsonify

from app.main.service.telegram import TelegramService


telegram_blueprint = Blueprint('telegram', __name__)


@telegram_blueprint.route('/<string:username>/', methods=['GET'])
def get_messages_by_username(username):
    offset_id = int(request.args.get('offset_id', 0))

    service = TelegramService()
    messages = service.get_messages(username=username, offset_id=offset_id)

    res = {
        'messages': messages
    }

    return jsonify(res)

