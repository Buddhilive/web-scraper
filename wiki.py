from bs4 import BeautifulSoup
import requests

url = 'https://si.wikipedia.org/wiki/ශ්%E2%80%8Dරී_දළදා_මාළිගාව'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'lxml')

content = doc.find("div", {"id": "mw-content-text"})

def main():
    createFile()

def createFile():
    with open('dist/content.txt', mode="w", encoding="utf-8") as f:
        f.write(content.text)
        titleName = doc.find('span', {'class': 'mw-page-title-main'}).text
        print(f'Document for {titleName} Created')

# Run the scrapper
main()