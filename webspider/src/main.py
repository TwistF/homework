#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: main.py
@time: 2020/6/14  17:06
"""

import bs4
import datetime
import traceback
import requests
from retrying import retry
from src import db_connect
from src import calculate
from threading import Thread


class CrawlerQueue(object):
    wait_q = []   # 待访问队列
    html_q = []   # 网页源码队列

    def getwaiturl(self):
        return CrawlerQueue.wait_q.pop(0)

    def addwait_q(self, url):
        CrawlerQueue.wait_q.append(url)

    def addhtml_q(self, html):
        CrawlerQueue.html_q.append(html)

    def gethtml_q(self):
        return CrawlerQueue.html_q.pop(0)

    def wait_q_count(self):
        return len(CrawlerQueue.wait_q)


class Crawler(object):
    def __init__(self, url_list):
        self.que = CrawlerQueue()
        for url in url_list:
            self.que.addwait_q(url[0])
            # print(self.que.wait_q)



    def crawler(self):
        url = self.que.getwaiturl()
        if url is None or url == "":
            return
        self.gethtml(url)

    def gettime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def do_log(self, e):
        try:
            with open('log.txt', "a") as f:
                e = self.gettime()+e
                f.write(e+"\n")    # 在文件中追加内容
        except Exception as ee:
            print(ee)

    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=3000)
    def gethtml(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
        }
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding

            self.que.addhtml_q(r.content)   # get ok
            self.getlink()
        except Exception as e:
            if "timed" in str(e) or "远程主机强迫关闭" in str(e):
                self.que.addwait_q(url)   # 访问超时，放回待访问队列，之后再访问
                print("访问超时")
            #traceback.print_exc()
            self.do_log(str(e))
            # print(e)

    def getlink(self): # 获取信息
        src = self.que.gethtml_q() # 网页源码部分
        try:
            soup = bs4.BeautifulSoup(src, features='lxml')
            result_list = soup.findAll("span", {"class":"t4"})  # 列表
            # print(result_list)
            connections = db_connect.connect()
            for i in result_list:
                if i.string == None or i.string == "薪资":
                    continue
                db_connect.write_salaries(i.string, connections[1], connections[0])
        except Exception as e:
            self.do_log(str(e))
            traceback.print_exc()
            print(e)

    def run(self):
        if len(self.que.wait_q) > 0:
            self.crawler()


if __name__ == '__main__':
    connections = db_connect.connect()
    url_list = db_connect.read_urls(connections[1], connections[0])
    craw = Crawler(url_list)
    while True:   # 多线程访问网页
        if len(craw.que.wait_q) > 0:
            t = Thread(target=craw.run())
            t.start()
        else:
            print("检索完成")
            break
    calculate.ans()