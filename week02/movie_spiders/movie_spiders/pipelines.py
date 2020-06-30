# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from movie_spiders.conf import config
from movie_spiders.utils import sql_engine


class MovieSpidersPipeline:

    def process_item(self, item, spider):
        if spider.name == 'douban':
            content = f"|{item['db_movie_name']}|\t|{item['db_movie_link']}|\t|{item['db_movie_detail']}|\n\n"
            with open('/Users/xiaoyu.gao/PycharmProjects/Python001-class01/week01/db_movie.txt', 'a', encoding='utf8') \
                    as f:
                f.write(content)
        elif spider.name == 'maoyan':
            sql_engine.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PWD, db=config.DB)
            sql = 'INSERT INTO {table} (`movie_name`, `movie_type`, `movie_release_tm`) VALUES (%s,%s,%s)'\
                .format(table=config.TABLE)
            sql_engine.execute(sql, [item['my_movie_name'], item['my_movie_type'], item['my_movie_release_tm']])
        return item
