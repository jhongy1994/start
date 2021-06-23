from bs4 import BeautifulSoup 
from selenium import webdriver 
from pprint import pprint

driver = webdriver.Chrome('/Users/jiyounghong/tobedev/chromedriver')

driver.get("https://www.starbucks.co.kr/menu/drink_list.do")

html_source = driver.page_source

soup = BeautifulSoup(html_source, 'html.parser')

products = soup.select('.product_list dd a')

pprint(products)
