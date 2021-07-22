import json
from request import Request
from mongo import MongoDB


class Specifications:
    """"
    get specification of each mobile
    """
    @staticmethod
    def get_specifications():
        mongo = MongoDB()
        database = mongo.database

        images = []

        # you have to open the file of each brand for get their mobile specification
        with open('link/samsung.json', 'r') as s:
            link = json.loads(s.read())

        for li in link:

            document = {}
            tables = {}
            features = {}
            url = f"https://www.gsmarena.com/{li}"

            response = (Request.request(url))
            phone_name = response.find('h1').text
            if '.' in phone_name:
                phone_name = ''.join(phone_name.split('.'))

            print(phone_name)

            image = response.find('div', {'class': 'specs-photo-main'})
            photo_link = (image.find('img').get('src'))
            images.append(photo_link)
            print(photo_link)

            find_div = response.find('div', {'id': 'specs-list'})
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
            print(document)
            collections = database['samsung1']
            collections.insert_one(document)
        # this file  is for images of main page of each mobile
        with open('image/samsung-image.json', 'w') as s:
            s.write(json.dumps(images))
