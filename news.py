from bs4 import BeautifulSoup
import requests

url = 'https://www.bbc.com/sinhala/world-62924463'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'lxml')

content = doc.find("main")

def main():
    createFile()

def createFile():
    with open('dist/news.txt', mode="w", encoding="utf-8") as f:
        f.write(content.text)
        titleName = doc.find('h1', {'id': 'content'}).text
        print(f'Document for {titleName} Created')

# Run the scrapper
main()