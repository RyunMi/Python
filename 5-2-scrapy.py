import scrapy


class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://mofanpy.com/',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls 正则表达式有问题
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically