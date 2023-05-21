from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, send_from_directory
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        quotes = [
            "Testing Shit 1.",
            "It is not titles that honor men, but men that honor titles.",
            "The lion cannot protect himself from traps, and the fox cannot defend himself from wolves. One must therefore be a fox to recognize traps, and a lion to frighten wolves..",
            "Believe you can and you're halfway there.",
            "The future belongs to those who believe in the beauty of their dreams."
        ]
        return jsonify({'quotes': quotes})

api.add_resource(Quotes, '/quotes')

@app.route('/')
def index(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
