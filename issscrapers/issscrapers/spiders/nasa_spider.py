import scrapy


class NasaSpider(scrapy.Spider):
    name = "sightings"
    start_urls = [
        'https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=England&city=Liverpool'
    ]

    def parse(self, response):
        sighting = []
        for returned_item in response.css('td::text').getall():
            # append relevant returned_items
            if "\n" not in returned_item:
                sighting.append(returned_item)

            # End of individual sighting reached
            if len(sighting) == 5:
                # Yield items in each list to a dictionary
                yield {
                    'date': sighting[0],
                    'visible':sighting[1],
                    'max height':sighting[2],
                    'appears':sighting[3],
                    'disappears':sighting[4],
                }
                #reset sighting
                sighting = []