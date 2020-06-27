#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup
from traceback import format_exc


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Cookie': '__mta=45847323.1592914357761.1592914817372.1592915986013.5; uuid_n_v=v1; '
              'uuid=D7F55B90B54A11EAAED76517B51C0C67E8C6815B95F74ADEA2DF428308928C2B; '
              '_csrf=21df5fa6d0f4168ef24985e23d2e038719c888790a2259434baf63cf0cc36ae4; '
              '_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172e1182b5ac8-085802a7cbf047-'
              '143c6251-13c680-172e1182b5ac8; _lxsdk=D7F55B90B54A11EAAED76517B51C0C67E8C6815B95F74ADEA2DF428308928C2B; '
              'mojo-uuid=79cbe094d1ad831c76a0f40e2cdf3c3a; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592916676,'
              '1592916678,1592916714,1592916767; mojo-session-id={"id":"30c9e23ff0310ba3fb206e5d5b5574c6",'
              '"time":1592963759705}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592963760; '
              '__mta=45847323.1592914357761.1592915986013.1592963759794.6; _lxsdk_s=172e409fe77-ea9-008-4ff%7C%7C2'
}


def parse_content(content):
    movies_info = list()
    try:
        soup = BeautifulSoup(content, 'html.parser')
        movies = soup.find('dl', attrs={'class': 'movie-list'}).find_all('dd')
        for _ in movies[:10]:
            movie_info = _.find('div', attrs={'class': 'movie-hover-info'})
            movie_name = movie_info.find('span', attrs={'class': 'name'}).get_text()
            movie_type = movie_info.find_all('div', attrs={'class': 'movie-hover-title'})[1]\
                .get_text().replace('类型:\n', '').strip()
            movie_release_tm = movie_info.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'})\
                .get_text().replace('上映时间:\n', '').strip()
            tmp_list = [movie_name, movie_type, movie_release_tm]
            print(movie_name, movie_type, movie_release_tm)
            movies_info.append(tmp_list)
        return True, movies_info
    except Exception as e:
        return False, format_exc()


def get_movies(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        succ, movies_info = parse_content(resp.content)
        if not succ:
            print('parse content except::%s', movies_info)
            return
        pf = pd.DataFrame(movies_info)
        pf.to_csv('./movie.csv', encoding='utf8', index=False, header=False)
    except Exception as e:
        print('get movies except:%s', format_exc())


if __name__ == '__main__':
    url = 'https://maoyan.com/films?showType=3'
    get_movies(url)
