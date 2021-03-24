import scrapy
import datetime
from pharmacy.items import PharmacyItem
from scrapy.loader import ItemLoader


class PharmacySpider(scrapy.Spider):
    name = 'pharmacy-gemini'
    allowed_domains = ['aptekagemini.pl']
    start_urls = ['https://www.aptekagemini.pl/kategoria/kosmetyki/']

    def parse(self, response):
        for product in response.css('.product-card__container'):
            item_loader = ItemLoader(item=PharmacyItem(), selector=product)
            item_loader.add_css('name', '.product-card__name-wrapper')
            item_loader.add_css('price', '.money-price__amount')
            item_loader.add_css('link', 'a.product-card__link::attr(href)')
            item_loader.add_value('time', str(datetime.datetime.now()))
            item_loader.add_value('pharmacy', str(PharmacySpider.name))

            yield item_loader.load_item()

        next_page = response.css(
            'a.pagination__step.pagination__step--next::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
