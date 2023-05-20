const quoteElement = document.getElementById('quote');
const inputElement = document.getElementById('input');

async function getRandomQuote() {
    const response = await fetch('http://localhost:5000/quotes');
    const data = await response.json();
    const quotes = data.quotes;
    console.log("Received quotes",quotes);
    const index = Math.floor(Math.random() * quotes.length);
    return quotes[index];
}

async function displayQuote() {
  const randomQuote = getRandomQuote();
  console.log(randomQuote);
  randomQuote.then(quote => {
    quoteContainer.innerText = quote;
  });
}

// displayQuote()

document.addEventListener('DOMContentLoaded', function() {
  displayQuote();
});

inputElement.addEventListener('input', function() {
    if (inputElement.value === quoteElement.textContent) {
      inputElement.value = '';
      displayQuote();
    }
});
