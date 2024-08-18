from flask import Flask,make_response, jsonify

app = Flask(__name__)

from model import db
@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Welcome To The World of Flask</h1>'

@app.route('/api/items',methods=['GET'])
def getAllProducts():  # put application's code here
    return make_response(jsonify({"products":db}),200);


if __name__ == '__main__':
    app.run()
