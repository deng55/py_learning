from scrapy import Spider

from work.python网络数据采集.chapter03.wikiSpider import Article


class ArticleSpider(Spider):
    name = "article"
    allow_domains = ['en.wikipedia.org']
    start_urls = ["http://en.wikipedia.org/wiki/Main_page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("title is: " + title)
        item["title"] = title
        return item
    #
    # from scrapy.contrib.spiders import CrawlSpider, Rule
    # from wikiSpider.items import Article
    # from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    # class ArticleSpider(CrawlSpider):
    #     name = "article"
    #
    # allowed_domains = ["en.wikipedia.org"]
    # start_urls = ["http://en.wikipedia.org/wiki/Python_
    #               % 28programming_language % 29"]
    #               rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'), ),
    #                             callback="parse_item", follow=True)]
    #
    # def parse_item(self, response):
    #     item = Article()
    #
    # title = response.xpath('//h1/text()')[0].extract()
    # print("Title is: " + title)
    # item['title'] = title
    # return item
