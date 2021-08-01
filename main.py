from Specifications import Specifications
from crawler import CrawlerLinks

import sys

from pictures import Pictures

if __name__ == "__main__":
    # instead of this you can call get_maker_link method in Link class and assign the value to find_maker_link
    find_maker_link = ['samsung-phones-9.php', 'apple-phones-48.php', 'xiaomi-phones-80.php']

    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = CrawlerLinks()
        crawler.start()

    # pictures = Pictures()
    # pictures.get_link()
    # pictures.get_picture()
