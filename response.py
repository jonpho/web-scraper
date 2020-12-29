import requests
import pprint
from bs4 import BeautifulSoup

class Request:
    
    def __init__(self, url):
        self.url = url

    def getRequest(self):
        return requests.get(self.url)

    def getPageContent(self):
        return BeautifulSoup(self.getRequest().content, 'html.parser')
    
    def pageFindAll(self, element):
        return self.getPageContent().find_all(element)
