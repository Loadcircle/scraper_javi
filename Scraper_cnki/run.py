from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas
import tqdm
import re
import timeit
import time
import json
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver", chrome_options=options)

url = 'http://new.oversea.cnki.net/kns/brief/result.aspx?dbprefix=SCDB'

driver.get(url)

#uncheck all unnecesary filters
driver.find_element_by_name('(A) Mathematics/ Physics/ Mechanics/ Astronomy').click()
driver.find_element_by_name('(B) Chemistry/ Metallurgy/ Environment/ Mine Industry').click()
driver.find_element_by_name('(C) Architecture/ Energy/ Traffic/ Electromechanics, etc').click()
driver.find_element_by_name('(D) Agriculture').click()
driver.find_element_by_name('(E) Medicine & Public Health').click()
driver.find_element_by_name('(I) Electronic Technology & Information Science').click()
#uncheck all unnecesary filters



buscador = driver.find_element_by_id('txt_1_value1')
buscador.send_keys("秘鲁")

driver.find_element_by_id('btnSearch').click()

print('buscando')




# driver.implicitly_wait(20) # seconds
time.sleep(20)
# driver.implicitly_wait(20) # seconds
print('pasados 20 segundos')

html_from_page = driver.page_source

soup = BeautifulSoup(html_from_page, 'html.parser')

#table = soup.findAll("table")

#print(len(table))
#print(table)
#print(table[1].find("tr"))

#print(",".join([th.text for th in table[1].find("tr").find_all("th")]))


print(soup.findAll("iframe")[1])

iframe = soup.findAll("iframe")[1]

time.sleep(3)
## You have to switch to the iframe like so: ##

print(driver.find_element_by_tag_name("iframe"))

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

html_from_page2 = driver.page_source

print(html_from_page2)

time.sleep(3)

button = driver.find_element_by_class_name('GridTableContent')

print(button)




# driver.implicitly_wait(20) # seconds


myDynamicElement = driver.find_element_by_id("J_ORDER")

print(myDynamicElement)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "J_ORDER"))
#     )
#     print('loaded')
# finally:
#     driver.quit()

driver.close()


