# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas


class MovieSpidersPipeline:

    def process_item(self, item, spider):
        if spider.name == 'douban':
            content = f"|{item['db_movie_name']}|\t|{item['db_movie_link']}|\t|{item['db_movie_detail']}|\n\n"
            with open('/Users/xiaoyu.gao/PycharmProjects/Python001-class01/week01/db_movie.txt', 'a', encoding='utf8') \
                    as f:
                f.write(content)
        elif spider.name == 'maoyan':
            movie_info = pandas.DataFrame([(item['my_movie_name'], item['my_movie_type'], item['my_movie_release_tm'])])
            movie_info.to_csv('/Users/xiaoyu.gao/PycharmProjects/Python001-class01/week01/my_movie.csv',
                              mode='a', encoding='utf8', index=False, header=False)
        return item
