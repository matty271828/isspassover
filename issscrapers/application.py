import scrapy
from scrapy.crawler import CrawlerProcess
from issscrapers.spiders.nasa_spider import NasaSpider
    
if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(NasaSpider)
  process.start()