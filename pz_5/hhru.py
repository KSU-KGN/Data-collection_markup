import scrapy
from scrapy.http import HtmlResponse

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://kurgan.hh.ru/search/vacancy?hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&text=python&enable_snippets=false&L_save_area=true']

    def parse(self, response:HtmlResponse):
        # name - response.xpath("//span[@data-qa = 'serp-item__title']")
        next_page = response.xpath("//a[@data-qa = 'pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("///span[@class = 'serp-item__title-link-wrapper']//@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath("//h1/text()").get()
        salary = response.xpath(("//div[@data-qa = 'vacancy-salary']//text()")).getall()
        url = response.url

        print(response.status, response.url)
        ### pass

