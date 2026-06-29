# Zillow Clone Scraper & Data Entry Automation

This project is a Python script that automates the process of collecting rental property data and entering it into a database (Google Forms). 

The program consists of two main parts:
1. **Web Scraping:** Extracts data (prices, addresses, and links) from a website (Zillow Clone) using `BeautifulSoup`.
2. **Data Entry Automation:** Automatically opens a browser using `Selenium` and fills the extracted data into a pre-created Google Form.

## Built With

* **Python 3**
* **BeautifulSoup 4** - For parsing HTML and extracting data from the website.
* **Requests** - For downloading the web page.
* **Selenium WebDriver** - For browser automation and form submission.

## ⚙️ Installation and Setup

```bash
pip install requests beautifulsoup4 selenium