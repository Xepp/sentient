import json
import numpy as np
from flask import Flask
from flask import request
from dataset import get_dataset
from preprocess import text_cleaner
from model import LinearSVCModel
from model import SparseModel


app = Flask(__name__)

X_train, Y_train, X_test, Y_test = get_dataset(['sina_v1.csv', 'sina_v2.csv'])
X_train = X_train.map(text_cleaner)
X_test = X_test.map(text_cleaner)
X_train = np.asarray(X_train)
Y_train = np.asarray(Y_train)
X_test = np.asarray(X_test)
Y_test = np.asarray(Y_test)

#  model = LinearSVCModel()
model = SparseModel()
model.load_or_train(X_train, Y_train, X_test, Y_test)


@app.route("/",  methods=['POST'])
def index():
    data = request.get_json()
    predicted = model.predict(data['sentences'])

    return json.dumps({ 'predicted': list(predicted) }), 200, { 'ContentType': 'application/json' }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
