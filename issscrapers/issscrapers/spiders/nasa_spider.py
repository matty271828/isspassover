import scrapy


class NasaSpider(scrapy.Spider):
    name = "sightings"
    start_urls = [
        'https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=England&city=Liverpool'
    ]

    def parse(self, response):
        for sighting in response.css('td::text').getall():
            yield {
                'sighting': sighting,
            }