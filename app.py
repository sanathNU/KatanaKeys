from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, send_from_directory
from flask_restful import Api, Resource
import random, time, atexit
import pandas as pd
from  QuotesHelper import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

CORS(app)

class Quotes(Resource):
    def get(self):
        # quotes = readQuotesfromFile('Quotes/quotes.txt'
        # quotes = getQuotes()
        quotes = readWordsFile('Quotes/10000-english.txt')
        return jsonify({'quotes': quotes})

api.add_resource(Quotes, '/quotes')

# Defining all global variables
SaveLocation = ''
GameStats = {'QuotesLength': [],
              'WPM': [],
              'InGameSpeeds': []}

@app.route('/')
def index():
    # Creating a file name with current date and time
    global SaveLocation
    DataFileName = time.strftime("%Y%m%d-%H%M%S") + '.csv'
    SaveLocation = 'userstats/' + DataFileName
    return render_template('index.html')

# Stores the final session user stats in a .csv file
def writeUserStats():
    df = pd.DataFrame(GameStats)
    df.to_csv(SaveLocation,index=False)

# Saving the stats later for data analysis
@app.route('/currentsession',methods=['POST'])
def handle_session():
    # Extracting the list of in-game speeds
    values = request.json
    GameStats['QuotesLength'].append(values['WIQ'])
    GameStats['WPM'].append(values['typingSpeeds'][-1])  
    GameStats['InGameSpeeds'].append('-'.join(list(map(str,values['typingSpeeds']))))
    # print(values,GameStats)

    return 'OK'

# At end of flask app calls function to write down the stats
# atexit.register(writeUserStats)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
