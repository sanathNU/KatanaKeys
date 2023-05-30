# KatanaKeys
This is a small scale project for a typing website, where users can try their typing test. 
Planning to do as a 3 phase project. Should start working on the architecture of this.

## Introduction
The main goal of this website, it to give an interactive typing website with random quotes that are uncensored by any goal with the intent of typing a paragraph of any topic of choice.

## Architecture
Planned to be developed in 3 phases

### Phase 1
* ~~Simple typing website with a fixed number of quotes.~~
* ~~Connect python to the javascript to get more number of quotes that can be accessed dynamically.~~
* Use python API to get more data from quote websites.

### Phase 2
* Develop analysis of the data of wpm done by the users and present it as a graph. Or a time series
* Run a linear regression model on then number of words vs speed and accuracy graph.
* Add a safe filter for texts, which can be vulgur and add a sign that warns

### Phase 3
* Create an option for genres of different types of quotes.
* Scrap from everything. Create an LLM model that spits out good stuff depending on the user's workablility.

### How to Use
1. Basically, first clone the github repository <br>
`git clone https://github.com/sanathNU/KatanaKeys.git `
2. If wanted, create a virtual environment using venv and activate the virtual environment.
3. Run the python flask app using the following command <br>
` python app.py ` <br>
The app should start running and can be accessed by entering ` http://localhost:5000 ` on browser.


## Tools, Libraries
## Features
## TODO

## Resources from
1. Quotes.txt file taken from https://gist.github.com/erickedji
