const puppeteer = require("puppeteer");

const scrape = async () => {
    let result = null;

    try {
        const browser = await puppeteer.launch({
            headless: true,
            ignoreHTTPSErrors: true,
            defaultViewport: {
                width: 1200,
                height: 900
            }
        });
        const page = await browser.newPage();
        await page.goto("https://books.toscrape.com/");

        result = await page.$$eval("h3 > a", el => el.map(x => x.getAttribute("title")));

        console.log("bookTitles: ", result);

        await browser.close();
    } catch (error) {
        console.log("#### ERR: ", error)
    }
    return result
};

module.exports = {
    scrape
};

