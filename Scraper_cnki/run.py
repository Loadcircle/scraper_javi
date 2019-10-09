from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas
import tqdm
import re
import timeit
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


driver.implicitly_wait(30) # seconds


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


