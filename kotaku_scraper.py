from utilities import Utilities
from response import Request

url = 'https://kotaku.com/c/news'
article = []
kotaku_page = Request(url)
results = kotaku_page.page_find_all('article')

def kotaku_date_cleanup(pulled_date):
    pulled_date_with_year = Utilities.add_year_to_current_date(pulled_date)
    cleaned_date = Utilities.convert_date_format(pulled_date_with_year)
    return cleaned_date
    
for result in results:
    current_article = result
    article_dict = {}
    try:
        print(current_article.h2.text)
        print(current_article.find_all('a')[1]["href"])
        print(current_article.find_all('div')[1].text)
        article_dict['title'] = current_article.h2.text
        article_dict['link'] = current_article.find_all('a')[1]["href"]
        article_dict['date'] = kotaku_date_cleanup(current_article.find_all('div')[1].text)
        
        article.append(article_dict)
    except AttributeError:
        print("No article info in article")

print(article)