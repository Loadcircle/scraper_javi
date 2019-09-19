from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
import tqdm
import re
import timeit

url = 'http://ilas.cass.cn/ens_new/publicaciones/rdel/'

content = requests.get(url).content

resolve_content = BeautifulSoup(content, 'lxml')

div = resolve_content.findAll('div', {'class': 'cbw_list'})

urls = []

for i in div[0].findAll('a', href=True):
    urls.append('http://ilas.cass.cn/ens_new/publicaciones/rdel' + i['href'][1:])

final_url = []

for u in urls:
    c = requests.get(u).content
    r = BeautifulSoup(c, 'lxml')
    print(r)








# print(div[0])

# for i in div[0].findAll('p') or div[0].findAll('div'):

#     if i.text != '':
#         print(i.text)