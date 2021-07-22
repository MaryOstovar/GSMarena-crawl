import json
from request import Request


class Pictures:
    """"
    get all pictures link of each mobile
    """

    @staticmethod
    def get_link():
        link_pic_page = []

        with open('link/samsung.json', 'r') as s:
            link = json.loads(s.read())

        for li in link:
            url = f"https://www.gsmarena.com/{li}"

            response = (Request.request(url))
            print(response)
            find_div = response.find('div', {'class': 'article-info-line page-specs light'})
            print(find_div)
            if find_div is None:
                continue
            tag_a = find_div.find_all('a')
            if tag_a is None:
                continue
            for tag in tag_a:
                links = tag.get('href')
                if "pictures" in links:
                    print(links)
                    link_pic_page.append(links)

        with open('image/samsung_relative.json', 'w') as x:
            x.write(json.dumps(link_pic_page))

    @staticmethod
    def get_picture():

        with open("image/samsung_relative.json", 'r') as f:
            pic_link = (json.loads(f.read()))

        for li in pic_link:
            picture = []
            url = f"https://www.gsmarena.com/{li}"
            response = (Request.request(url))

            find_div = response.find('div', {'id': 'pictures-list'})
            if find_div is None:
                continue

            phone_name = find_div.find('img')
            phone_name = phone_name.get('alt')
            print(phone_name)
            pic = find_div.find_all('img')
            print(pic)
            for img in pic:
                picture.append(img.get('src'))

            with open(f"img/{phone_name}.json", 'w')as f:
                f.write(json.dumps(picture))
