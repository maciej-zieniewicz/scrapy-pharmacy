import scrapy
import datetime
from pharmacy.items import PharmacyItem
from scrapy.loader import ItemLoader


class PharmacySpider(scrapy.Spider):
    name = 'pharmacy-doz'
    allowed_domains = ['doz.pl']
    start_urls = ['https://www.doz.pl']

    def parse(self, response):
        for category in response.css('.menu__item .link--dark'):
            category_page = 'https://www.doz.pl' + category.attrib['href']
            if 'Kosmetyki'.lower() in category_page.lower():
                yield scrapy.Request(category_page, callback=self.parse_category)

    def parse_category(self, response):
        for products in response.css('li.product__list-item.product'):

            item_loader = ItemLoader(item=PharmacyItem(), selector=products)
            item_loader.add_css('name', 'a.link--dark-orange::attr(title)')
            item_loader.add_css('price', 'a.btn.btn--wide')
            item_loader.add_css('link', 'a.link--dark-orange::attr(href)')
            item_loader.add_value('time', str(datetime.datetime.now()))
            item_loader.add_value('pharmacy', str(PharmacySpider.name))

            yield item_loader.load_item()

        next_page = response.css(
            'a.pagination__site.pagination__site--next::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_category)
