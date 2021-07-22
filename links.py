import json
from request import Request


class Link:

    @staticmethod
    def get_maker_link(link):  # from source get each company relative url
        find_maker_link = []
        source = Request.request(link)

        find_div = source.find('div', {'class': 'st-text'})
        find_all_tag_a = find_div.findAll('a')

        for tr in find_all_tag_a:
            find_maker_link.append(tr.get('href'))

        return find_maker_link

    @staticmethod
    # get each mobile link and save in separate file for each brand
    def get_each_link_mobile(url, relative_link):
        find_link_mobile = []
        source = Request.request(url)

        find_div = source.find('div', {'class': 'makers'})
        find_link_maker = find_div.findAll('a')

        for tr in find_link_maker:
            find_link_mobile.append(tr.get('href'))

        if relative_link == 'samsung-phones-9.php':
            with open('link/samsung.json', 'w') as s:
                s.write(json.dumps(find_link_mobile))
            find_link_mobile.clear()

        if relative_link == 'apple-phones-48.php':
            with open('link/apple.json', 'w') as a:
                a.write(json.dumps(find_link_mobile))
            find_link_mobile.clear()

        if relative_link == 'xiaomi-phones-80.php':
            with open('link/xiaomi.json', 'w') as x:
                x.write(json.dumps(find_link_mobile))
            find_link_mobile.clear()
