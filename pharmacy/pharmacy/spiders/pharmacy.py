import scrapy
import datetime
from pharmacy.items import PharmacyItem
from scrapy.loader import ItemLoader


class PharmacySpider(scrapy.Spider):
    name = 'pharmacy'
    allowed_domains = ['doz.pl']
    start_urls = ['https://www.doz.pl/apteka/k4889-Wyprzedaze',
                  'https://www.doz.pl/apteka/k4873-Leki_na_recepte',
                  'https://www.doz.pl/apteka/k4300_17-Bol',
                  'https://www.doz.pl/apteka/k4348-Kosmetyki',
                  'https://www.doz.pl/apteka/k4944-Serce_i_krazenie',
                  'https://www.doz.pl/apteka/k4615-Przeziebienie_i_grypa',
                  'https://www.doz.pl/apteka/k4633-Seks_i_zdrowie_intymne',
                  'https://www.doz.pl/apteka/k4819-Sprzet_medyczny',
                  'https://www.doz.pl/apteka/k4600-Trawienie',
                  'https://www.doz.pl/apteka/k4315-Witaminy_i_mineraly',
                  'https://www.doz.pl/apteka/k4755-Zielarnia']

    def parse(self, response):
        for products in response.css('li.product__list-item.product'):
            item_loader = ItemLoader(item=PharmacyItem(), selector=products)

            item_loader.add_css('name', 'a.link--dark-orange::attr(title)')
            item_loader.add_css('price', 'a.btn.btn--wide')
            item_loader.add_css('link', 'a.link--dark-orange::attr(href)')
            item_loader.add_value('time', str(datetime.datetime.now()))

            yield item_loader.load_item()

        next_page = response.css(
            'a.pagination__site.pagination__site--next::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
