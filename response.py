import requests
import pprint
from bs4 import BeautifulSoup

class Request:
    
    def __init__(self, url):
        self.url = url

    def get_request(self):
        # Function sends the initial request to the URL wanted for scraping.
        return requests.get(self.url)

    def get_page_content(self):
        # Function will take the intial get request and then parse out the html for searching.
        return BeautifulSoup(self.get_request().content, 'html.parser')
    
    def page_find_all(self, element):
        # Function sorts out the tags or elements wanted for data scraping.
        return self.get_page_content().find_all(element)
