from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Elizabeth_II'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

content = doc.find("div", {"id": "mw-content-text"})

# print(content.prettify())

# print(content.text)

# print(content.encode("utf-8"))

def createFile():
    with open('dist/content.txt', mode="w", encoding="utf-8") as f:
        f.write(content.text)