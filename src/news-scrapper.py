from bs4 import BeautifulSoup
import requests
import os

url_collection = [
    'https://www.bbc.com/sinhala/topics/c83plvepnq1t?page='
]

folder_collection = [
    'world'
]

ref_id = 0

baseurl = url_collection[ref_id]
page_count = 40
folder_name = folder_collection[ref_id]

count = 1
missed_urls = list()

def findArticleLinks():
    for page in range(page_count):
        feed_link = f"{baseurl}{page + 1}"

        result = requests.get(feed_link)
        page_data = BeautifulSoup(result.text, 'lxml')

        content_raw = page_data.find("main")
        content_all = content_raw.find_all('div', { "class": "promo-text" })

        print(f"Scrapping started for Page: {page + 1}")
        count = 1
        for link in content_all:
            raw_link = link.find('a')
            extractText(raw_link.get('href'))
            # print(raw_link.get('href'))

        # print(len(content_all), page)


def extractText(url):
    try:
        result = requests.get(url)

        doc = BeautifulSoup(result.text, 'lxml')
        # titleName = doc.find('h1', {'id': 'content'}).text
        fileName = url.replace('https://www.bbc.com/sinhala/', '')
        fileName = fileName.replace('/', '-')

        content_raw = doc.find("main")

        content_all = content_raw.find_all('p')

        content = ''

        for text in content_all:
            content += text.text
            # print(text.text)

        createFile(content, fileName)
    except:
        missed_urls.append(url)
        with open('dist/log.txt', mode="w", encoding="utf-8") as f:
            for line in missed_urls:
                f.write(" ".join(line) + "\n")
        print(f"An exception occurred in {url}")


def createFile(content, fileName):
    global count
    # checking if the directory demo_folder2 
    # exist or not.
    if not os.path.isdir(f'dist/news/{folder_name}'):
    
        # if the demo_folder2 directory is 
        # not present then create it.
        os.makedirs(f'dist/news/{folder_name}')

    with open(f'dist/news/{folder_name}/{fileName}.txt', mode="w", encoding="utf-8") as f:
        f.write(content)
        print(f'[{count}] Document {fileName} Created')
        count += 1

def main():
    findArticleLinks()

# Run the scrapper
main()