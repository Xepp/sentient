import json

from flask import Flask
from flask import request

from model import Model


app = Flask(__name__)
model = Model()

@app.route("/",  methods = ['POST'])
def index():
    data = request.get_json()
    predicted = model.predict(data['sentences'])

    return json.dumps({ 'predicted': list(predicted) }), 200, { 'ContentType': 'application/json' }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

