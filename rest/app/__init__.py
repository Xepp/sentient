import os
from flask import json
from werkzeug.exceptions import HTTPException

from app.main import create_app


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

