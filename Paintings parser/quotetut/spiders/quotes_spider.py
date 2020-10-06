
import scrapy
from ..items import QuotetutItem

class QuoteSpider(scrapy.Spider):

    name = 'art'
    page_number = 2
    start_urls = [
        'https://www.saatchiart.com/paintings?page=1'
    ]

    def parse (self, response):
        all_paintings = response.css('.cfoXjx:nth-child(1) .kcNkMy a::attr(href)').extract()
        for i in range(len(all_paintings)):
            all_paintings[i] = 'https://www.saatchiart.com' + all_paintings[i]

        yield from response.follow_all(all_paintings, self.parse_painting)

        next_page = 'https://www.saatchiart.com/paintings?page={}'.format(QuoteSpider.page_number)
        if QuoteSpider.page_number <= 600:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)


    def parse_painting (self, response):

        items = QuotetutItem()

        image_url = response.css('meta[property = "og:image"]::attr(content)').extract()
        sizes = response.css('.grHICv::text').extract()
        styles = response.css('.bhxZbk:nth-child(6) a::text').extract()
        material = response.css('.bhxZbk:nth-child(8) a::text').extract()
        prod_type = response.css('meta[property = "og:type"]::attr(content)').extract()
        price = response.css('meta[property = "product:price:amount"]::attr(content)').extract()
        currency = response.css('meta[property = "product:price:currency"]::attr(content)').extract()

        items['image_url'] = image_url
        items['sizes'] = sizes
        items['styles'] = styles
        items['material'] = material
        items['product_type'] = prod_type
        items['price'] = price
        items['currency'] = currency

        yield items

