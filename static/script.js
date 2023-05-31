
// the link at which the quotes are posted
const quotesUrl = 'http://127.0.0.1:5000/quotes';
let quotesData = []; // random variable to store the fetched quotes

let wpmArray = [];

// Fetch the quotes from the Flask app
function fetchQuotes() {
    return fetch(quotesUrl)
    .then(response => response.json())
    .then(data => {
        quotesData = data.quotes;
    });
}
// Display a random quote from the fetched quotes
function displayRandomQuote() {
    const index = Math.floor(Math.random() * quotesData.length);
        const quote = quotesData[index];
        document.getElementById('quote-text').textContent = quote;
}
// updates typing speed as the user types
function updateTypingSpeed() {

    const quote = document.getElementById('quote-text');
    const endTime = new Date();
    const timeDiff = (endTime - startTime) / 1000; // in seconds
    const words = input.value.split(' ').length;
    const wpm = Math.round(words / (timeDiff / 60));

    // Display in-game typing speed
    document.getElementById('Ctyping-speed').textContent = `Typing speed: ${wpm} wpm`;
    // recording for in-game stats
    wpmArray.push(wpm);

}

// Check whether the input of the user is right or not
function checkQuote() {

    const quote = document.getElementById('quote-text');
    const WordsInQuote = quote
    .textContent.split(' ')
    .length;
    
    if (input.value == quote.textContent) {
    input.value = "";
    displayRandomQuote();
    //display previous speed
    const cTypingSpeed = document.getElementById('Ctyping-speed').textContent;
    const currentSpeed = cTypingSpeed.split(' ')[2]; // Extracting 3rd element

    document.getElementById('Ptyping-speed').textContent = `Previous Speed ${currentSpeed} wpm`;
    // Reset typing speed
    
    document.getElementById('Ctyping-speed').textContent = "";
    startTime = null;

    fetch('/currentsession', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({WIQ: WordsInQuote, typingSpeeds: wpmArray})
    })
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => {
        console.error('Error:', error); // Log and print the error to the console
    });

    // Reset wpmArray
    wpmArray = [];

    } else if (input.value.length === 1 && startTime === null) {
    // Start timer when user starts typing
    startTime = new Date();
    // Update typing speed every second
    setInterval(updateTypingSpeed, 1000);
    }
}
let startTime = null;

// first call for quotes
fetchQuotes().then(() => {
displayRandomQuote(); 
})
document.getElementById('Ptyping-speed').textContent = "Previous Speed 0 wpm";
input.addEventListener("input", checkQuote);