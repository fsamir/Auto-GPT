const booksScraper = require('./books-scraper');
(async () => {
    let books = await booksScraper.scrape();
    console.log("books: ", books);
})();

