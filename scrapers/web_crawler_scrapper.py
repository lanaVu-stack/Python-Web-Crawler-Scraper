# Python Web Crawler Scraper
# Uses Requests and BeautifulSoup to extract web crawler-related information from a webpage.


import requests
from bs4 import BeautifulSoup


url = "https://www.keycdn.com/blog/web-crawlers"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")


results = soup.find_all("h2")

print("DUCKDUCKBOT RESULTS")

for result in results:

    text = result.text

    if "DuckDuckBot" in text:

        print(text)

        paragraph = result.find_next("p")

        print(paragraph.text)


