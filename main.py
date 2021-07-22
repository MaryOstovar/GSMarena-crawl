from Specifications import Specifications
from links import Link


from pictures import Pictures
if __name__ == "__main__":
    # instead of this you can call get_maker_link method in Link class and assign the value to find_maker_link
    find_maker_link = ['samsung-phones-9.php', 'apple-phones-48.php', 'xiaomi-phones-80.php']

    # link_object = Link()
    # for link in find_maker_link:
    #     url = f"https://www.gsmarena.com/{link}"
    #     link_object.get_each_link_mobile(url, link)

    specification = Specifications()
    specification.get_specifications()

    pictures = Pictures()
    pictures.get_link()
    pictures.get_picture()
