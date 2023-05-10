'''
Script for parsting websites and getting random quotes that is then used by the typing website.
'''

import requests
from bs4 import BeautifulSoup
import json

# Send an HTTP request to the website and get the HTML response
url = 'https://www.brainyquote.com/topics/inspirational-quotes'
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the quote elements on the page and extract the text
quote_elements = soup.find_all('div', {'class': 'clearfix'})
quotes = [quote.find('a').text for quote in quote_elements]

# Save the quotes to a JSON file
with open('quotes.json', 'w') as f:
    json.dump(quotes, f)
