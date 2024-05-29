import scrapy
from scrapy.http import HtmlResponse

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://kurgan.hh.ru/search/vacancy?hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&text=python&enable_snippets=false&L_save_area=true']

    def parse(self, response:HtmlResponse):
        # name - response.xpath("//span[@data-qa = 'serp-item__title']")
        links = response.xpath("///span[@class = 'serp-item__title-link-wrapper']//@href").getall()
        for link in links:
            response.follow(link)
        
        print(response.status, response.url)
        ### pass

