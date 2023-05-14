const quoteElement = document.getElementById('quote');
const inputElement = document.getElementById('input');

async function getRandomQuote() {
    const response = await fetch('http://localhost:5000/quotes');
    const data = await response.json();
    const quotes = data.quotes;
    const index = Math.floor(Math.random() * quotes.length);
    return quotes[index];
}

async function displayQuote() {
  const randomQuote = getRandomQuote();
  randomQuote.then(quote => {
    quoteContainer.innerText = quote;
  });
}

document.addEventListener('DOMContentLoaded', function() {
  displayQuote();
});

inputElement.addEventListener('input', function() {
    if (inputElement.value === quoteElement.textContent) {
      inputElement.value = '';
      displayQuote();
    }
});
