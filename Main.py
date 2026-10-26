import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for item in soup.find_all("div", class_="quote"):
        quote = item.find("span", class_="text").get_text()
        author = item.find("small", class_="author").get_text()

        quotes.append({
            "quote": quote,
            "author": author
        })

    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=4, ensure_ascii=False)

    print("Quotes scraped successfully!")
    print("Total quotes:", len(quotes))
    print("Data saved in quotes.json")

except requests.RequestException as error:
    print("Error fetching website:", error)
