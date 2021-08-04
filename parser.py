from bs4 import BeautifulSoup

from mongo import MongoDB


class SpecificationParser:

    def parse(self, html_duc):
        document = {}
        tables = {}
        features = {}

        phone_name = html_duc.find('h1').text
        if '.' in phone_name:
            phone_name = ''.join(phone_name.split('.'))

        find_div = html_duc.find('div', {'id': 'specs-list'})
        find_table = find_div.findAll('table')

        for table in find_table:

            table_name = table.find('th', {'scope': 'row'}).text
            for tr in table.find_all('tr'):
                td_ttl = getattr(tr.find('td', {'class': 'ttl'}), 'text', None)

                if td_ttl is None:
                    td_ttl = 'sample'

                elif '.' in td_ttl:
                    td_ttl = ''.join(td_ttl.split('.'))

                td_nfo = getattr(tr.find('td', {'class': 'nfo'}), 'text', None)
                features.update({td_ttl: td_nfo})

            tables.update({table_name: features})
            features = {}
        document.update({'phone': phone_name})
        document.update({'features': tables})
        return document
