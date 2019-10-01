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

final_url = []

contador = 1
contador_2 = 1

def make_request():
    global contador
    print('try number '+ str(contador) + ' remaining connections ' + str(len(urls)))
    for idx, u in enumerate(urls):
        try:
            if requests.get(u, timeout=(5,5)).status_code == 200:
                c = requests.get(u, timeout=(5,5)).content
                r = BeautifulSoup(c, 'lxml')
                s = r.findAll('script')[0].string
                a = re.findall(r'"(.*?)"', s)                
                final_url.append(urls[idx] + a[0][2:])                
                urls.remove(u)
                print(a)

        except:
            print('no response')
            
    if len(urls) > 0 and contador < 10:
        contador += 1
        make_request()

make_request()

print(final_url)

final_text = []

objecto = {
            'Titulo': [],
            'Fecha': [],
            'Keyword': [],
            }

# final_url = ['http://ilas.cass.cn/ens_new/publicaciones/rdel/rdel/2016/04/201701/t20170110_3378232.shtml', 'http://ilas.cass.cn/ens_new/publicaciones/rdel/rdel/2011/04/201109/t20110901_2265972.shtml']

def make_request_2():
    global contador_2
    print('try number '+ str(contador_2) + ' remaining connections ' + str(len(final_url)))
    for fu in final_url:

        try:

            fu_c = requests.get(fu).content

            resolve_fu = BeautifulSoup(fu_c, 'lxml')

            div_fu = resolve_fu.findAll('div', {'class': 'content_body'})

            if len(div_fu) > 0:

                for z in div_fu[0].findAll('p') or div_fu[0].findAll('div') or div_fu[0].findAll('a'):

                    if z.text != '' and re.findall(r'^.*\bAbstract\b.*$', z.text) < 1:

                        objecto['Titulo'].append(z.text)
                                    
                        fecha = resolve_fu.findAll('div', {'class': 'ct_time'})

                        if len(fecha) > 0:

                            objecto['Fecha'].append(fecha[0].text)

                        else:
                            objecto['Fecha'].append('')
                        
                        match = re.search(r'\bBrazil|\bPeru|\bPerú|\bMexico|\bColombia|\bArgentina|\bEcuador|\bBolivia|\bParaguay|\bUruguay|\bCosta\sRica|\bPanama|\bHaiti|\bHaiti|\bNicaragua|\bGuatemala|\bVenezuela|\bCuba', z.text, re.I)
                        
                        if match:
                            objecto['Keyword'].append(match.group())
                        else:
                            objecto['Keyword'].append('Latinoamerica')

            final_url.remove(fu)

        except:
            print('no response')

    if len(final_url) > 0 and contador_2 < 10:
        contador_2 += 1
        make_request_2()

make_request_2()

# print(objecto)

df = DataFrame(objecto, columns=['Titulo', 'Fecha', 'Keyword'])

print(df)

try:
    export_csv = df.to_csv (r'C:\Users\PC\Desktop\final_result_s_tries.csv', index = None, header=True, encoding='utf_32') #Don't forget to add '.csv' at the end of the path
    print('Archivo exportado')

except Exception as e: 
    print(e)

print('------------------------End-------------------')
print('Remaining conections: ' + str(len(urls)) + ' Remaining Final Url ' + str(len(final_url)))

print(urls)
print('-----------------------------------------------------------------')
print(final_url)