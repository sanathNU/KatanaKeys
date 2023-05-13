// const quotes = [
//     "Life is like riding a bicycle. To keep your balance, you must keep moving.",
//     "The only way to do great work is to love what you do.",
//     "Success is not final, failure is not fatal: it is the courage to continue that counts.",
//     "Believe you can and you're halfway there.",
//     "The future belongs to those who believe in the beauty of their dreams."
//   ];
 

  const quote = document.getElementById("quote");
  const input = document.getElementById("input");
  
  // Old function, to be replaced by new stuff
  // function getRandomQuote() {
  //   const index = Math.floor(Math.random() * quotes.length);
  //   return quotes[index];
  // }

  function getRandomQuote() {
    return fetch('/quotes')
        .then(response => response.json())
        .then(data => data.quotes)
        .then(quotes => {
            const index = Math.floor(Math.random() * quotes.length);
            return quotes[index];
        });
}

  
  function displayQuote() {
    const randomQuote = getRandomQuote();
    quote.textContent = randomQuote;
  }
  
  displayQuote();
  
  input.addEventListener("input", function() {
    if (input.value === quote.textContent) {
      input.value = "";
      displayQuote();
    }
  });
  