import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://pokemonkorea.co.kr/pokedex'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

count = 16

# 처음 데이터
info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist li')

info_list = info_list[-count:]

html_text = ''
for item in info_list:
    tag = item.get_attribute('outerHTML')
    html_text += tag
    
soup = BeautifulSoup(html_text, 'html.parser')


for item in soup:
    h3_list = item.select('h3')