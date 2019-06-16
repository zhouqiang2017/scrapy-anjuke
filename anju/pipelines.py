# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import re

client = MongoClient()
collection = client['anjuke']['village']


class AnjuPipeline(object):
    def process_item(self, item, spider):
        item['name'] = self.process_name(item['name'])
        item['summary'] = self.process_summary(item['summary'])
        print(item)
        collection.insert(dict(item))
        return item

    @staticmethod
    def process_name(name):
        name = [re.sub(r"\n|\t", '', i) for i in name]
        name = [i for i in name if len(i) > 0]
        name = "".join(name)
        return name

    @staticmethod
    def process_summary(summary):
        summary = [re.sub(r"\n|\t", '', i) for i in summary]
        summary = [re.sub(r"\u3000|\r", '', i) for i in summary]
        summary = [i for i in summary if len(i) > 0]
        summary = "".join(summary)
        return summary
