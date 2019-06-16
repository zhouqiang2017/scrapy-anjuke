# -*- coding: utf-8 -*-
import scrapy
from anju.items import AnjuItem


class VillageSpider(scrapy.Spider):
    name = 'village'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://chengdu.anjuke.com/community/?from=navigation']

    def parse(self, response):
        villages_dom = response.xpath("//div[@class='li-itemmod']")
        for dom in villages_dom:
            item = AnjuItem()
            item['href'] = dom.xpath("./div[1]/h3[1]/a[1]/@href").extract_first()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item': item}
            )
        # 翻页 首先找到下一页的url
        next_url = response.xpath("//a[@class='aNxt']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item['name'] = response.xpath("//div[@class='comm-title']/h1[1]/text()").extract_first()
        item['address'] = response.xpath("//div[@class='comm-title']/h1[1]/span[1]/text()").extract_first()
        item['house_type'] = response.xpath("//dl[@class='basic-parms-mod']/dd[1]/text()").extract_first()
        item['property_fee'] = response.xpath("//dl[@class='basic-parms-mod']/dd[2]/text()").extract_first()
        item['total_area'] = response.xpath("//dl[@class='basic-parms-mod']/dd[3]/text()").extract_first()
        item['total_family'] = response.xpath("//dl[@class='basic-parms-mod']/dd[4]/text()").extract_first()
        item['build_year'] = response.xpath("//dl[@class='basic-parms-mod']/dd[5]/text()").extract_first()
        item['carport'] = response.xpath("//dl[@class='basic-parms-mod']/dd[6]/text()").extract_first()
        item['plot_ratio'] = response.xpath("//dl[@class='basic-parms-mod']/dd[7]/text()").extract_first()
        item['green_ratio'] = response.xpath("//dl[@class='basic-parms-mod']/dd[8]/text()").extract_first()
        item['developer'] = response.xpath("//dl[@class='basic-parms-mod']/dd[9]/text()").extract_first()
        item['tenement'] = response.xpath("//dl[@class='basic-parms-mod']/dd[10]/text()").extract_first()
        item['business_district'] = response.xpath("//dl[@class='basic-parms-mod']/dd[11]/text()").extract_first()
        item['summary'] = response.xpath("//div[@class='comm-brief-mod j-ext-infos']/p[1]/text()").extract()
        item['image'] = response.xpath("//div[@class='item']/img/@src").extract()
        # print(item['summary'])
        yield item
