'''
Script for parsting websites and getting random quotes that is then used by the typing website.
'''

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/quotes')
def get_quotes():
    # Send an HTTP request to the website and get the HTML response
    # url = 'https://api-ninjas.com/api/quotes'
    # response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    # soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the quote elements on the page and extract the text
    # quote_elements = soup.find_all('div', {'class': 'clearfix'})
    # quote_list = [quote.find('a').text for quote in quote_elements]

    quotes_list = [
    "Testing Shit 1.",
    "It is not titles that honor men, but men that honor titles.",
    "The lion cannot protect himself from traps, and the fox cannot defend himself from wolves. One must therefore be a fox to recognize traps, and a lion to frighten wolves..",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in the beauty of their dreams."]

    quotes = {"quotes":quote_list}
    return jsonify(quotes)

# test = get_quotes()