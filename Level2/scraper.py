# Level 2 - Task 2
# Data Scraper (Quotes Scraper)
# Codveda Python Internship

import requests
from bs4 import BeautifulSoup
import csv


def scrape_quotes():
    url = "http://quotes.toscrape.com"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author"])

            for quote in quotes:
                text = quote.find("span", class_="text").text
                author = quote.find("small", class_="author").text
                writer.writerow([text, author])

        print("✅ Data scraped successfully and saved to quotes.csv")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching the webpage:", e)
    except Exception as e:
        print("❌ An unexpected error occurred:", e)


# Program execution starts here
scrape_quotes()
