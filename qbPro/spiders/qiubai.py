# -*- coding: utf-8 -*-
import scrapy,hashlib
from qbPro.items import QbproItem
from redis import Redis

# 只爬取当前页面
class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'

    conn = Redis(host='127.0.0.1',port=6379)
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="content-left"]/div')
        for div in div_list:
            # 数据指纹:爬取到一条数据的唯一标识
            author = div.xpath('./div/a[2]/h2/text() | ./div/span[2]/h2/text()').extract_first().strip()
            content = div.xpath('./a/div/span[1]//text()').extract()
            content = ''.join(content).replace('\n','')
            item = QbproItem()  # 实例化
            item['author'] = author
            item['content'] = content

            # 给爬取到的数据生成一个数据指纹
            data = author+content
            hash_key = hashlib.sha256(data.encode()).hexdigest()
            ex = self.conn.sadd('hash_key',hash_key)  # 输指纹存进 集合里面
            if ex == 1:
                print('有数据更新')
                yield item
            else:
                print('无数据更新')


