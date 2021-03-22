import scrapy
from pharmacy.items import PharmacyItem
from scrapy.loader import ItemLoader


class PharmacySpider(scrapy.Spider):
    name = 'pharmacy'
    start_urls = ['https://www.doz.pl/apteka/k4889-Wyprzedaze']

    def parse(self, response):
        for products in response.css('li.product__list-item.product'):
            item_loader = ItemLoader(item=PharmacyItem(), selector=products)

            item_loader.add_css('name', 'a.link--dark-orange::attr(title)')
            item_loader.add_css('price', 'a.btn.btn--wide')
            item_loader.add_css('link', 'a.link--dark-orange::attr(href)')

            yield item_loader.load_item()

        next_page = response.css(
            'a.pagination__site.pagination__site--next::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
