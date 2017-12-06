# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import urllib

# 爬取页面地址
url = 'http://www.mm131.com/xinggan/3378.html'

# 目标元素的xpath
xpath = '/html/body/div[6]/div[2]/a/img'

# 启动Firefox浏览器
#driver = webdriver.Firefox(executable_path = '/Users/liaohuanghe/Downloads/geckodriver')
driver = webdriver.Chrome(executable_path='/Users/liaohuanghe/Downloads/driver/chromedriver_mac32_64')

# 最大化窗口，因为每一次爬取只能看到视窗内的图片
driver.maximize_window()

# 记录下载过的图片地址，避免重复下载
img_url_dic = {}

# 浏览器打开爬取页面
driver.get(url)

# 模拟滚动窗口以浏览下载更多图片
pos = 0
m = 0  # 图片编号
i = 0
#pos += i * 500  # 每次下滚500
#js = "document.documentElement.scrollTop=%d" % pos
#driver.execute_script(js)
#time.sleep(1)

for element in driver.find_elements_by_xpath(xpath):
    img_url = element.get_attribute('src')
    # 保存图片到指定路径
    if img_url != None:
        img_url_dic[img_url] = ''
        m += 1
        ext = img_url.split('.')[-1]
        filename = str(m) + '.' + ext
        # 保存图片数据
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url=img_url, headers=headers)
        res = urllib.request.urlopen(req)

        data = res.read()
       # data = urllib.request.urlopen(img_url).read()
        f = open('/Users/liaohuanghe/PycharmProjects/PrettyCrawler/pic/' + filename, 'wb')
        f.write(data)
        f.close()
driver.close()
