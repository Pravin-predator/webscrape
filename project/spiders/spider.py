import scrapy
from ..items import WebscrapeItem


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        items = WebscrapeItem()
        for quote in response.css("div.quote"):

                items['text'] = quote.css('span.text::text').extract()
                items['author']= quote.css('small.author::text').extract()
                items['tags'] = quote.css('div.tags > a.tag::text').extract()

                yield items

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
