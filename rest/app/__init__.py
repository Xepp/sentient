import os
from flask import json
from flask import Blueprint
from flask_restx import Api
from werkzeug.exceptions import HTTPException
from app.main import create_app
from app.main.controller.instagram import api as instagram_namespace
from app.main.controller.twitter import api as twitter_namespace
from app.main.controller.web import api as web_namespace
from app.main.controller.telegram import api as telegram_namespace


env = 'prod' if os.getenv('FLASK_ENV') == 'production' else 'dev'
app = create_app(env)


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description
    })
    response.content_type = 'application/json'

    return response


blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='Gecko',
          version='1.0',
          description='Crawler of persian social media')

api.add_namespace(instagram_namespace, path='/api/instagram')
api.add_namespace(twitter_namespace, path='/api/twitter')
api.add_namespace(web_namespace, path='/api/web')
api.add_namespace(telegram_namespace, path='/api/telegram')


app.register_blueprint(blueprint)
