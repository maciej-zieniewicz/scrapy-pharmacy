import scrapy


class PharmacySpider(scrapy.Spider):
    name = 'pharmacy'
    start_urls = ['https://www.doz.pl/apteka/k4889-Wyprzedaze']

    def parse(self, response):
        for products in response.css('li.product__list-item.product'):
            yield {
                'name': products.css('a.link--dark-orange').attrib['title'],
                'price': products
                .css('a.btn.btn--wide.product__price::text')
                .get().replace('zł', '').replace('\n', '')
                .strip(),
                'link': products.css('a.link--dark-orange').attrib['href']
            }
        try:
            next_page = 'https://www.doz.pl' + \
                response.css(
                    'a.pagination__site.pagination__site--next').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except Exception:
            print('End of pages')
