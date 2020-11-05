from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort

from app.main.service.web import KhabarFooriService


web_blueprint = Blueprint('web', __name__)


@web_blueprint.route('/khabar-foori/', methods=['GET'])
def get_khabar_foori_comments():
    url = request.args.get('url', None)

    if url is None:
        abort(404, description='Page not found')

    service = KhabarFooriService()
    comments = service.get_comments(url=url)

    res = {
        'comments': comments
    }

    return jsonify(res)

