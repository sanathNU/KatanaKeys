from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, send_from_directory
from flask_restful import Api, Resource
import random
from  QuotesHelper import *

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        # quotes = readQuotes('Quotes/quotes.txt')
        quotes = getQuotes()
        return jsonify({'quotes': quotes})

api.add_resource(Quotes, '/quotes')

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/currentsession',methods=['POST'])
def handle_session():
    speeds = request.json
    print(request.data)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
