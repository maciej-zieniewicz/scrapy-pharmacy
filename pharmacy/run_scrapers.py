
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


import pharmacy.spiders.pharmacy_doz as doz
import pharmacy.spiders.pharmacy_gemini as gemini

process = CrawlerProcess(settings=get_project_settings())
process.crawl(doz.PharmacySpider)
process.crawl(gemini.PharmacySpider)
process.start()
