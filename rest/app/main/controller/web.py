from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort

from app.main.service.web import KhabarFooriService
from app.main.service.athena import AthenaService


web_blueprint = Blueprint('web', __name__)


@web_blueprint.route('/khabar-foori/', methods=['GET'])
def get_khabar_foori_comments():
    url = request.args.get('url', None)

    if url is None:
        abort(404, description='Page not found')

    service = KhabarFooriService()
    comments = service.get_comments(url=url)

    text_list = []
    for cm in comments:
        text_list.append(cm['text'])
        for reply in cm['replays']:
            text_list.append(reply['text'])
    athena_service = AthenaService()
    sentiment = athena_service.get_predicted_sentiment(text_list)
    index = 0
    for cm in comments:
        cm['sentiment'] = sentiment[index]
        index += 1
        for reply in cm['replays']:
            reply['sentiment'] = sentiment[index]
            index += 1

    res = {
        'comments': comments
    }

    return jsonify(res)
