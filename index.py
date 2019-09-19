from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
import tqdm
import re
import timeit

url = 'http://ilas.cass.cn/ens_new/publicaciones/rdel/rdel/2003/01'

content = requests.get(url).content

print(content)

resolve_content = BeautifulSoup(content, 'lxml')

div = resolve_content.findAll('div', {'class': 'content_body'})

# print(div[0])

# for i in div[0].findAll('p') or div[0].findAll('div'):

#     if i.text != '':
#         print(i.text)