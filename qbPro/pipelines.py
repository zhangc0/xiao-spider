# -*- coding: utf-8 -*-

class QbproPipeline(object):
    def process_item(self, item, spider):
        conn = spider.conn
        dic = {
            'author': item['author'],
            'content': item['content']
        }
        conn.lpush('qiubai', str(dic))
        return item
