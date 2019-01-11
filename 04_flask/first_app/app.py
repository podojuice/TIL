from flask import Flask, jsonify

import random


app = Flask(__name__)



@app.route('/')
def index():
    return 'Hi1'

@app.route('/ssafy')
def ssafy():
    return 'ssssssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return f'hi! {name}'




if __name__ == '__main__':
    app.run(debug=True)

