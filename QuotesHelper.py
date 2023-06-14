# Libraries to be imported
import wikiquote
import random
import csv

## Function to open the quotes.txt file and read through the contents
def readQuotesfromFile(path_to_file):
    # reading the file
    quotesFile = open(path_to_file,'r',encoding='utf-8',errors='ignore')
    lines = quotesFile.readlines()
    quotes=[]

    flag, q = 0, ''
    for line in lines:
        if '--' in line:
            author = line.split(',')[0].replace('--','').strip()
            # print(t)
            quotes.append({author:q.strip()})
            q = ''
        else:
            q+=line.strip() + ' '

    return quotes

## Function to open file 10000-english.txt and create a random sentences using these words
def readWordsFile(path_to_file):
    # Reading from file
    wordsFile = open(path_to_file,'r')
    words = [x.strip() for x in wordsFile.readlines()]
    randSentences = []

    # creating a set of random sentences from random words
    for i in range(200):
        sentLen = random.randint(1,50)
        sentence = random.sample(words,sentLen)
        randSentences.append(' '.join(sentence))
    
    return randSentences
   

## Function to get quotes from wikiquotes website using the api provided
def getQuotes():
    titles = wikiquote.random_titles(max_titles=10)

    quotes = []
    for title in titles:
        quotes.extend([x.strip()+' ' for x in wikiquote.quotes(title)])
    random.shuffle(quotes)

    return quotes

readWordsFile('Quotes/10000-english.txt')