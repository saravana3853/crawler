from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import db

from selenium.webdriver.common.by import By


def crawl_web():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options)
    url = "https://news.ycombinator.com/"
    driver.get(url)
    time.sleep(3)
    elements = driver.find_elements(By.CLASS_NAME, 'athing')
    y_combinator_news = []

    for e in elements:
        try:
            news_dict = {}
            rank=e.find_element(By.CLASS_NAME,'rank')
            el=e.find_element(By.CLASS_NAME,'titleline')
            href=el.find_element(By.TAG_NAME,'a').get_attribute("href")
            sitestr=el.find_element(By.CLASS_NAME,'sitestr')
            #print(rank.text+";"+el.text+";"+href+";"+sitestr.text)
            news_dict['rank']=rank.text
            news_dict['href']=href
            news_dict['domain']=sitestr.text
            news_dict['title']=el.text
            #print("\n")
            y_combinator_news.append(news_dict);
            print(y_combinator_news)
        except:
            print('error in one of news item')

    db.bulk_insert(y_combinator_news)
