import json
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

from config import BASE_LINK, storage_type, api


class CrawlerBase(ABC):
    def __init__(self):
        self.storage = storage_type

    @abstractmethod
    def start(self, *args, **kwargs):
        pass

    @staticmethod
    def request(url):  # request & make object of Beautiful-soup

        try:
            response = api.get(url)
            soup = BeautifulSoup(response['body'], 'html.parser')
            return soup

        except ConnectionError as ce:
            print(ce)


class CrawlerLinks(CrawlerBase):
    def __init__(self, link=BASE_LINK):
        super().__init__()
        self.base_link = link

    def start(self):
        companies_link = self.get_maker_link(self.base_link)
        for links in companies_link:
            url = f"https://www.gsmarena.com/{links}"
            mobile_link = self.get_each_link_mobile(url)
            self.storage.store(mobile_link, links)

    def get_maker_link(self, link):  # from source get each company relative url
        find_maker_link = []
        source = self.request(link)

        find_div = source.find('div', {'class': 'st-text'})
        find_all_tag_a = find_div.findAll('a')

        for tr in find_all_tag_a:
            find_maker_link.append(tr.get('href'))

        return find_maker_link

    # get each mobile link and save in separate file for each brand
    def get_each_link_mobile(self, url):
        find_link_mobile = []
        source = self.request(url)

        find_div = source.find('div', {'class': 'makers'})
        find_link_maker = find_div.findAll('a')

        for tr in find_link_maker:
            find_link_mobile.append(tr.get('href'))
        return find_link_mobile
