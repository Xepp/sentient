from flask import request
from flask import jsonify
from flask import abort
from flask_restx import Resource
from app.main.dto.web import WebDTO

from app.main.service.web import KhabarFooriService
from app.main.service.athena import AthenaService


api = WebDTO.api
res = WebDTO.response


@api.route('/khabar-foori/')
class KhabarFooriComments(Resource):
    @api.response(200, 'Comments returned successfully.', res)
    @api.doc('fetch comments based on url',
             params={
                 'url': {
                     'description': 'url of khabar foori website post detail',
                     'in': 'query',
                     'type': 'string',
                     'required': True
                  }
             })
    def get(self):
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
