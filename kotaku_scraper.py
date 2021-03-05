from base_scraper import BaseScraper
from utilities import Utilities
from response import Request


class KotakuPage(BaseScraper):
    
    def __init__(self, url, param):
        BaseScraper.__init__(self, url, param)

    def kotaku_date_cleanup(self, pulled_date):
        pulled_date_with_year = Utilities.add_year_to_current_date(pulled_date)
        cleaned_date = Utilities.convert_date_format(pulled_date_with_year)
        return cleaned_date
    
    def kotaku_results(self, results):
        for result in results:
            current_article = result
            article_dict = {}
            try:
                print(current_article.h2.text)
                print(current_article.find_all('a')[1]["href"])
                print(current_article.find_all('div')[1].text)
                article_dict['title'] = current_article.h2.text
                article_dict['link'] = current_article.find_all('a')[1]["href"]
                article_dict['date'] = self.kotaku_date_cleanup(current_article.find_all('div')[1].text)
                
                self.article.append(article_dict)
            except AttributeError:
                print("No article info in article")


p = KotakuPage('https://kotaku.com/c/news', 'article')
p.kotaku_results(p.results)
print(p.article)