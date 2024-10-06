import scrapy
from urllib.parse import urlencode
from bs4 import BeautifulSoup

def get_scraperapi_url(url):
    APIKEY = "YOUR_SCRAPERAPI_KEY"
    payload = {'api_key': APIKEY, 'url': url, 'render': True}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

class ZaraProductSpider(scrapy.Spider):
    name = "zara_products"
    def start_requests(self):
        urls = [
            'https://www.zara.com/ww/en/man-shirts-l737.html?v1=2351464',
            'https://www.zara.com/ww/en/man-shirts-l737.html?v1=2351464&page=2',
            'https://www.zara.com/ww/en/man-shirts-l737.html?v1=2351464&page=3'
        ]
        for url in urls:
            yield scrapy.Request(url=get_scraperapi_url(url), callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for product in soup.select('div.product-grid-product-info'):
            product_name = product.select_one('h2').get_text(strip=True) if product.select_one('h2') else None
            price = product.select_one('span.money-amount__main').get_text(strip=True) if product.select_one('span.money-amount__main') else None
            yield {
                'product_name': product_name,
                'price': price,
            }