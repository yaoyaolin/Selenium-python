#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib
import requests
import re,json

page = []
url = "http://www.shoplooks.com/retailer"
data = requests.get(url)
print(data.text)
#content = re.findall(r'g_page_config = (.*?)g_srp_loadCss',data.text,re.S)[0]
