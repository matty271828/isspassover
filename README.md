# isspassover

This web-scraper makes use of the Python web crawling framework Scrapy in order to check a Nasa maintained webpage detailing times and directions of passes of the Internation Space Station above the location of a user. 

For Scrapy to function, a spider class is created which created which uses HTML tags to retrieve select strings from the webpage. This is information is then outputted to a .JSON file. 
