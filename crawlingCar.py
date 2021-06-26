from bs4 import BeautifulSoup
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
driver.get('****************')
html_source = driver.page_source
soup = BeautifulSoup(html_source,'html.parser')

cates = soup.select('.s_1  option')
cate = [cate.string for cate in cates]

for i in range(2,4):
    category_x = driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[2]/select/option[%d]'%(i))
    category_x.click()
    time.sleep(1)
    category = cate[i-1]
    soup = BeautifulSoup(driver.page_source,'html.parser')
    brands = soup.select('.s_2 option')
    brand = [brand.string for brand in brands]
    for k in range(2,len(brand)+1):
        brand_x = driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[3]/select/option[%d]'%(k))
        brand_x.click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        models = soup.select('.s_3 option')
        model = [model.string for model in models]
        # print(category,brand[k-1],model)
        for x in range(2,len(model)+1):
            model_x = driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[4]/select/option[%d]'%(x))
            model_x.click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[6]/a').click()
            time.sleep(5)
            try:
                numt = driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/a[4]').get_attribute('href')
                if numt!='javascript:;':
                    num = int(numt.split("'")[1])
                    # print(num)
                else:
                    num = 1
            except:
                num = 1
                continue
            # driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/a[4]').click()
            # time.sleep(5)
            # num = driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/strong').text
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'aucEndListResult')))
            # print(category,brand[k-1],model[x-1])
            container = dict()
            result = []
            # for p in range(1,num):
            for p in range(0,num):
                soup = BeautifulSoup(driver.page_source, 'html.parser')          
                try:
                    lists = soup.select('.aucEndListResult tr')
                    for list in lists:
                        tit = list.find_all(class_='tit ta_c')
                        container['date'] = tit[0].get_text(strip=True)
                        container['category'] = category
                        container['brand'] = brand[k-1]
                        container['model'] = model[x-1]
                        container['info'] = list.find(class_='fwb fs16').text
                        container['fuel'] = list.find(class_='mt10 fs12').text
                        container['acc'] = tit[1].get_text(strip=True)
                        container['year'] = tit[2].get_text(strip=True)
                        container['trvl'] = tit[3].get_text(strip=True)
                        container['price'] = list.find(class_='blue_txt fwb').text
                        result.append(container)
                        pprint(result)
                except:
                    print('fail')
                    continue
                driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/a[3]').click()
                time.sleep(3)

df = pd.DataFrame(result)
df.to_csv('./car.csv', index=False)
df.head()
