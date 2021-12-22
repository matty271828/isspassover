import scrapy
import json

class NasaSpider(scrapy.Spider):
    name = "sightings"
    start_urls = [
        'https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=England&city=Liverpool'
    ]

    def parse(self, response):
        # Open json file and add first bracket
        with open("sightings.json", "w") as file:
            file.write('[\n')

            # Instantiate variables
            sighting = []
            i = 0

            for returned_item in response.css('td::text').getall():
                # append relevant returned_items
                if "\n" not in returned_item:
                    sighting.append(returned_item)

                # End of individual sighting reached
                if len(sighting) == 5:
                    # Write each item to the file
                    json.dump({
                        'date': sighting[0],
                        'visible':sighting[1],
                        'max height':sighting[2],
                        'appears':sighting[3],
                        'disappears':sighting[4],
                    }, file)
                    # Reset sighting
                    sighting = []

                    # 3 subtracted to account for extraeneous returned items
                    if i != len(response.css('td::text').getall()) - 5:
                        # New line
                        file.write(",\n")
                    else:
                        file.write("\n")

                i = i + 1
      
            # Add final bracket        
            file.write(']')