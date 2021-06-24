from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import time
import pandas as pd

#웹드라이버 실행
driver = webdriver.Chrome('./chromedriver.exe')
#사이트 접근
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')
#html소스 가져오기
html_source = driver.page_source
#beautifulsoup이용해서 html파싱
soup = BeautifulSoup(html_source, 'html.parser')
#원하는 정보 선택
products = soup.select('.product_list dd a')
#pprint사용하면 print보다 가독성 좋게 출력
#pprint(products)
#products에서 원하는 필드값만 추출
prod_cd = [[product['prod'], product.find('img')['alt']] for product in products]
# pprint(prod_cd)
result=[]
for prod in prod_cd:
    container = dict()
    cd = prod[0]
    name = prod[1]
    driver.get("https://www.starbucks.co.kr/menu/drink_view.do?product_cd={prod_cd}".format(prod_cd=cd))
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    # volume = soup.select_one('.product_info_head #product_info01').get_text()

    kcal = soup.select_one('.product_info_content .kcal dd').get_text() 
    sat_FAT = soup.select_one('.product_info_content .sat_FAT dd').get_text() 
    protein = soup.select_one('.product_info_content .protein dd').get_text() 
    fat = soup.select_one('.product_info_content .fat dd').get_text() 
    trans_FAT = soup.select_one('.product_info_content .trans_FAT dd').get_text() 
    protein = soup.select_one('.product_info_content .protein dd').get_text() 
    sodium = soup.select_one('.product_info_content .sodium dd').get_text() 
    sugars = soup.select_one('.product_info_content .sugars dd').get_text() 
    caffeine = soup.select_one('.product_info_content .caffeine dd').get_text() 
    cholesterol = soup.select_one('.product_info_content .cholesterol dd').get_text() 
    chabo = soup.select_one('.product_info_content .chabo dd').get_text() 
    container['cd'] = cd 
    container['name'] = name 
    container['kcal'] = kcal 
    container['sat_FAT'] = sat_FAT 
    container['protein'] = protein 
    container['fat'] = fat 
    container['trans_FAT'] = trans_FAT 
    container['protein'] = protein 
    container['sodium'] = sodium 
    container['sugars'] = sugars 
    container['caffeine'] = caffeine 
    container['cholesterol'] = cholesterol 
    container['chabo'] = chabo 
    result.append(container)

    # time.sleep(3)
pprint(result)
df = pd.DataFrame(result)

df.to_csv('./starbucks.csv', index=False)

print(df.head())
