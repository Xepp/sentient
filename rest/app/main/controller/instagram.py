from flask import Blueprint
from flask import request
from flask import jsonify

from app.main.service.instagram import InstagramService


instagram_blueprint = Blueprint('instagram', __name__)


@instagram_blueprint.route('/<string:shortcode>/', methods=['GET'])
def get_comments_by_shortcode(shortcode):
    end_cursor = request.args.get('end_cursor', None)

    ig_service = InstagramService()
    comments, new_end_cursor, has_next_page = ig_service.get_comments(shortcode=shortcode, end_cursor=end_cursor)

    res = {
        'comments': comments,
        'has_next_page': has_next_page,
        'new_end_cursor': new_end_cursor
    }

    return jsonify(res)

