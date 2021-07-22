from config import api
from bs4 import BeautifulSoup


class Request:
    @staticmethod
    def request(url):  # request & make object of Beautiful-soup

        try:
            response = api.get(url)
            soup = BeautifulSoup(response['body'], 'html.parser')
            return soup

        except ConnectionError as ce:
            print(ce)
