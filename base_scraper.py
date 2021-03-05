from utilities import Utilities
from response import Request


class BaseScraper:
    
    def __init__(self, url, param):
        self.url = url
        self.page = Request(url)
        self.article = []
        self.results = self.page.page_find_all(param)
