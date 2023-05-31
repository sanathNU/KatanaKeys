from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, send_from_directory
from flask_restful import Api, Resource
import random
from  QuotesHelper import *

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        quotes = readQuotes('Quotes/quotes.txt')
        # quotes = getQuotes()
        return jsonify({'quotes': quotes})

api.add_resource(Quotes, '/quotes')

@app.route('/')
def index(): 
    return render_template('index.html')

# Saving the stats later for data analysis
@app.route('/currentsession',methods=['POST'])
def handle_session():
    # Extracting the list of in-game speeds
    values = request.json
    WordsInQuote = values['WIQ']
    InGameSpeeds = values['typingSpeeds']
    # InGameSpeeds = list(request.json.values())[0]
    print(values)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
