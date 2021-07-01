from typing import Container
from bs4 import BeautifulSoup, element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import time
import pandas as pd

#웹드라이버 실행
driver = webdriver.Chrome('./chromedriver.exe')
#사이트 접근
website = 'http://honestC'
driver.get(website)
html_source = driver.page_source
soup = BeautifulSoup(html_source,'html.parser')

prods = soup.select('.car-detail.ul-car-detail a')
prodList = [prod['href'] for prod in prods]
print(prodList)

for cd in prodList:
    container= dict()
    driver.get('http://*****.com/{prod_cd}'.format(prod_cd=cd))
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    name = soup.select_one('.car_name p').get_text()
    price = soup.select_one('.dealerinfo td span').get_text()
    infoList = soup.select('.carinfo tr')
    infoList[0].find
    pprint(infoList)
