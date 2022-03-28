# isspassover

### Background

This web-scraper makes use of the Python web crawling framework Scrapy in order to check a Nasa maintained webpage detailing times and directions of passes of the Internation Space Station above the location of a user. 

For Scrapy to function, a spider class is created which created which uses HTML tags to retrieve select strings from the webpage. This is information is then outputted to a .JSON file. 

### Screenshot 1 - Web page to be scraped

![Liverpool, England, United Kingdom _ Sighting Opportunity _ Spot The Station _ NASA](https://user-images.githubusercontent.com/65253959/160461120-1870161a-e36e-406a-8320-1704f1bb7fd6.jpg)

### Screenshot 2 - Example of sightings.json response file after successful scraping

<img width="1103" alt="Screenshot 2022-03-28 at 19 29 44" src="https://user-images.githubusercontent.com/65253959/160463479-89aac116-d8e1-4088-bf91-d15b0e7c85f9.png">
