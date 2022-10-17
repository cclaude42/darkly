#!/usr/bin/env python3

import logging, sys
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, url):
        self.url = url
        self.readmes = []


    def download_url(self, url):
        return requests.get(url).text


    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path != "../" and path != "README":
                path = urljoin(url, path)
                yield path


    def check_page(self, url):
        readme = self.download_url(url + "README")
        if readme not in self.readmes:
            print(readme)
            self.readmes.append(readme)


    def run(self):
        html = self.download_url(self.url)
        for count, url1 in enumerate(self.get_linked_urls(self.url, html)):
            html1 = self.download_url(url1)
            for url2 in self.get_linked_urls(url1, html1):
                html2 = self.download_url(url2)
                for url3 in self.get_linked_urls(url2, html2):
                    self.check_page(url3)
            print(f"{ count+1 }/26...")


if __name__ == '__main__':
    Crawler(url='http://192.168.56.102/.hidden/').run()