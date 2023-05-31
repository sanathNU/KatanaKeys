# Libraries to be imported
import wikiquote
import random

## Function to open the quotes.txt file and read through the contents
def readQuotes(path_to_file):
    # reading the file
    quotesFile = open(path_to_file,'r',encoding='utf-8',errors='ignore')
    lines = quotesFile.readlines()
    quotes=[]

    flag, q = 0, ''
    for line in lines:
        if '--' in line:
            quotes.append(q.strip())
            # print(q,'\n', line)
            q = ''
        else:
            q+=line.strip() + ' '

    return quotes

## Function to get quotes from wikiquotes website using the api provided
def getQuotes():
    titles = wikiquote.random_titles(max_titles=10)

    quotes = []
    for title in titles:
        quotes.extend([x.strip()+' ' for x in wikiquote.quotes(title)])
    random.shuffle(quotes)

    return quotes

def saveStats(perGameStats):
    pass
