from flask import request
from flask import jsonify
from flask_restx import Resource
from app.main.dto.instagram import InstagramDTO

from app.main.service.instagram import InstagramService
from app.main.service.athena import AthenaService


api = InstagramDTO.api
res = InstagramDTO.response


@api.route('/<string:shortcode>/')
@api.param('shortcode', 'The post shortcode identifier')
class InstagramComments(Resource):
    @api.response(200, 'Comments returned successfully.', res)
    @api.doc('fetch instagram post comments based on shortcode',
             params={'end_cursor': {
                 'description': 'end_cursor for pagination',
                 'in': 'query',
                 'type': 'string'
             }})
    def get(self, shortcode):
        end_cursor = request.args.get('end_cursor', None)

        ig_service = InstagramService()
        comments, new_end_cursor, has_next_page = ig_service.get_comments(shortcode=shortcode, end_cursor=end_cursor)

        text_list = [cm['text'] for cm in comments]
        athena_service = AthenaService()
        sentiment = athena_service.get_predicted_sentiment(text_list)
        for index, cm in enumerate(comments):
            cm['sentiment'] = sentiment[index]

        res = {
            'comments': comments,
            'has_next_page': has_next_page,
            'new_end_cursor': new_end_cursor
        }

        return jsonify(res)
