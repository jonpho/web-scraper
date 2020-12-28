import requests
import pprint
from bs4 import BeautifulSoup

url = 'https://kotaku.com/c/news'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('article')

article = []

for result in results:
    current_article = result
    article_dict = {}
    try:
        print(current_article.h2.text)
        print(current_article.find_all('a')[1]["href"])
        print(current_article.find_all('div')[1].text)
        article_dict['title'] = current_article.h2.text
        article_dict['link'] = current_article.find_all('a')[1]["href"]
        article_dict['date'] = current_article.find_all('div')[1].text
        article.append(article_dict)
    except AttributeError:
        print("No article info in article")

print(article)