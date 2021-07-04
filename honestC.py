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
website = 'http://honestC.com/'
driver.get(website)
time.sleep(1)
for i in range(2):
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/ul/li[1]/a').click()
    car_list = '//*[@id="content_data"]/div/ul'
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, car_list)))
    if i==1:
        driver.find_element_by_xpath('//*[@id="list-pagination"]/li[6]/a').click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, car_list)))
    html_source = driver.page_source
    soup = BeautifulSoup(html_source,'html.parser')
    prods = soup.select('.car-detail.ul-car-detail .car-info a')
    prodList = [prod['href'] for prod in prods]
    pprint(prodList)
    result = []
    for cd in prodList:
        container= dict()
        driver.get('http://honestC.com/{prod_cd}'.format(prod_cd=cd))
        time.sleep(3)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        container['website'] = website
        container['name'] = soup.select_one('.car_name p').get_text()
        container['price'] = soup.select_one('.car_price span').get_text()
        infoList = soup.select('.basic-info tr td')
        container['year'] = infoList[0].string
        container['registerDate'] = infoList[1].string
        container['fuel'] = infoList[2].string
        container['trans'] = infoList[3].string
        container['color'] = infoList[4].string
        container['drvDis'] = infoList[5].string
        container['carNum'] = infoList[6].string
        container['num'] = infoList[7].string
        container['cark'] = infoList[9].string
        sellerInfo = soup.select('.seller-info .type02 tr td')
        container['seller'] = sellerInfo[0].string
        container['phone'] = sellerInfo[1].string
        container['Id'] = sellerInfo[2].string
        container['company'] = sellerInfo[3].string
        # container['companytell'] = sellerInfo[3].string.split('|')[1]
        result.append(container)
        pprint(container)


df = pd.DataFrame(result)

df.to_csv('./honestC.csv', index=False)
print(df.head())

df2 = pd.read_csv('./honestCar.csv', delimiter=',')
df2['company'] = df2.company.str.split('｜').str[0]
print(df2.head())
