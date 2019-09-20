from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas
import tqdm
import re
import timeit
import json
from pandas import DataFrame

url = 'http://ilas.cass.cn/ens_new/publicaciones/rdel/'

content = requests.get(url).content

resolve_content = BeautifulSoup(content, 'lxml')

div = resolve_content.findAll('div', {'class': 'cbw_list'})

urls = []

for i in div[0].findAll('a', href=True):
    urls.append('http://ilas.cass.cn/ens_new/publicaciones/rdel' + i['href'][1:])

# final_url = [ ]

final_url = []

for idx, u in enumerate(urls):

    try:
        if requests.get(u, timeout=(5,5)).status_code == 200:
            c = requests.get(u, timeout=(5,5)).content
            r = BeautifulSoup(c, 'lxml')
            s = r.findAll('script')[0].string

            a = re.findall(r'"(.*?)"', s)
            
            final_url.append(urls[idx] + a[0][2:])
            
            print(a)

    except:
        print('no response')

print(final_url)

final_text = []

for fu in final_url:

    try:
        fu_c = requests.get(fu).content

        resolve_fu = BeautifulSoup(fu_c, 'lxml')

        div_fu = resolve_fu.findAll('div', {'class': 'content_body'})

        if(len(div_fu) != 0):

            for z in div_fu[0].findAll('p') or div_fu[0].findAll('div') or div_fu[0].findAll('a'):

                if z.text != '':
                    print(z.text)
                    final_text.append(z.text)

    except:
        print('no response')



df = DataFrame(final_url)

export_csv = df.to_csv (r'C:\Users\PC\Desktop\export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

print (df)