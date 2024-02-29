import requests
from scrapy.http import TextResponse
import csv


def book_info(url):
    response = requests.get(url)
    text = response.text
    scrapy_response = TextResponse(url=response.url, body=text, encoding='utf-8')
    category = scrapy_response.css('.breadcrumb a::text').getall()[2]
    book_name = ''.join(scrapy_response.xpath("//div[@class='col-sm-6 product_main']//h1//text()").extract())
    info = scrapy_response.xpath('//table//td//text()').extract()
    upc = info[0]
    product_type = info[1]
    price = info[2]
    availability = info[5]
    reviews = info[6]

    info_dict = {'Book Name': book_name,
                 'category': category,
                 'upc': upc,
                 'Product Type': product_type,
                 'Price': price,
                 'Availability': availability,
                 'reviews': reviews}
    return info_dict


for i in range(50):
    main_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get("https://books.toscrape.com/")
    text = response.text
    scrapy_response = TextResponse(url=response.url, body=text, encoding='utf-8')
    urls = scrapy_response.xpath('//h3//a//@href').extract()

    with open('book_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Book Name', 'category', 'upc', 'Product Type', 'Price', 'Availability', 'reviews']

        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csvwriter.writeheader()

        for url in urls:
            full_url = scrapy_response.urljoin(url)
            info_dict = book_info(full_url)

            csvwriter.writerow(info_dict)
            print(info_dict)