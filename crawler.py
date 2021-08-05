import json
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

from config import BASE_LINK, storage_type, api
from storage import FileStorage, MongoStorage
from parser import SpecificationParser


class CrawlerBase(ABC):
    def __init__(self):
        self.storage = self.choose_storage()

    @staticmethod
    def choose_storage():
        if storage_type == "file":
            return FileStorage()
        return MongoStorage()

    @abstractmethod
    def start(self, *args, **kwargs):
        pass

    @abstractmethod
    def store(self, *args, **kwargs):
        pass

    @staticmethod
    def get(url):  # request & make object of Beautiful-soup

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

    def start(self, store=False):
        companies_link = self.get_maker_link(self.base_link)
        for links in companies_link:
            url = f"https://www.gsmarena.com/{links}"
            mobile_link = self.get_each_link_mobile(url)
            if store:
                self.store([{'url': li, 'flag': False} for li in mobile_link])

    def store(self, data, *args):
        self.storage.store(data, 'mobile_links')

    def get_maker_link(self, link):  # from source get each company relative url
        find_maker_link = []
        source = self.get(link)

        find_div = source.find('div', {'class': 'brandmenu-v2'})
        print(find_div)
        find_tag_ul = find_div.find('ul')
        find_all_tag_a = find_tag_ul.find_all('a')

        for tag_a in find_all_tag_a:
            find_maker_link.append(tag_a.get('href'))

        return find_maker_link

    # get each mobile link and save in separate file for each brand
    def get_each_link_mobile(self, url):
        find_link_mobile = []
        source = self.get(url)

        find_div = source.find('div', {'class': 'makers'})
        find_link_maker = find_div.findAll('a')

        for tr in find_link_maker:
            find_link_mobile.append(tr.get('href'))
        return find_link_mobile


class DataCrawler(CrawlerBase):
    def __init__(self):
        super().__init__()
        self.link_crawler = CrawlerLinks()
        self.links = self.__load_link()
        self.parser = SpecificationParser()

    def __load_link(self):
        links = []
        for reletive_url in self.link_crawler.get_maker_link(BASE_LINK):
            links.extend(self.storage.load(reletive_url))

        return links

    def start(self, store=False):
        for li in self.links:
            response = self.get(BASE_LINK + li)
            data = self.parser.parse(response)
            if store:
                self.store(data, li)

    def store(self, data, filename):
        self.storage.store(data, filename)




