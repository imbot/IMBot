__author__ = 'grishma'

import sys
import feedparser
from com.imbot.db import mongodb

def read_rss(url):
  fp = feedparser.parse(url)
  for i in fp:
    top_id = fp['entries'][i]['id']
    top_title = fp['entries'][i]['title']
    top_link = fp['entries'][i]['links'][i]['href']
    feed = {"top_id" : top_id, "top_title": top_title, "top_link": top_link}
    mongodb.insertData(feed)

if __name__ == "__main__":
  ibnlive_top_news_rss_url = "http://ibnlive.in.com/ibnrss/top.xml"
  rss_data = read_rss(ibnlive_top_news_rss_url)
  imbot_db = mongodb.initializeDb()
  mongodb.getCollection()