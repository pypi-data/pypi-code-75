# -*- coding: utf-8 -*-
class Pipeline:
    def __init__(self):
        self.count = 0

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.count += 1

    def close_spider(self, spider):
        pass
