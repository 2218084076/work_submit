import scrapy

from proxypool.items import ProxypoolItem


class Spider(scrapy.spiders.Spider):
    name = 'mimvp'
    allowed_domains = ['mimvp.org']
    start_urls = [
        'https://proxy.mimvp.com/freeopen?proxy=out_hp',
        'https://proxy.mimvp.com/freeopen?proxy=out_hp&sort=p_ip&page=2',
        'https://proxy.mimvp.com/freeopen?proxy=out_hp&sort=p_ip&page=3',
        'https://proxy.mimvp.com/freeopen?proxy=out_hp&sort=p_ip&page=4',

    ]

    def parse(self, response, **kwargs):
        for sel in response.xpath('/html/body/div[2]/div/table/tbody/tr'):
            item = ProxypoolItem()  # 将其在setting中 指定为utf-8，JSON 输出将不会被转义
            item['ip'] = sel.xpath('td[2]/text()').extract()[0]
            item['country'] = sel.xpath('td[5]/text()').extract()[0]
            item['post'] = sel.xpath('td[4]/text()').extract()[0]
            yield item
