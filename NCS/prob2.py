# from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import time

no_list = []
name_list = []
img_src_list = []
# 받아올 데이터 리스트 초기화 
# 포켓몬 번호, 포켓몬 이름, 포켓몬 이미지 url

# 포켓몬 도감 사이트
url = 'https://pokemonkorea.co.kr/pokedex'

# 셀레니움 옵션 설정
# Q: 셀레니움이 뭐에요? 동적 웹크롤링 패키지
options = webdriver.ChromeOptions()
# 크롭탭 안보이게 설정하기(창 없는 모드)
options.add_argument("--headless=new")
# 드라이버 설정
# Q: options = options 설정 이유가 뭐에요? 
# A: 괄호 안에 options를 지정해줄 경우, add_argument한 옵션을 사용할 수 있음
driver = webdriver.Chrome(options=options)

# 포켓몬 데이터 크롤링 
driver.get(url)

now = 0

# 현재 화면에 나와있는 포켓몬 리스트
while True:
    
    pokemon_list = driver.find_elements(By.CSS_SELECTOR, "#pokedexlist li")

    now = len(pokemon_list)
    
    if now >= (18 * 7):
        break
    
    
    for pokemon in pokemon_list:
        img_src = pokemon.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        img_src_list.append(img_src)
        
        no = pokemon.find_element(By.CSS_SELECTOR, ".bx-txt > h3 > p").text
        no_list.append(no)    
        
        name = pokemon.find_element(By.CSS_SELECTOR, 'div.bx-txt > h3').text
        name_list.append(name[8:])
        
    # 스크롤 내리기 (JS)
    script = "document.body.scrollIntoView(false);"
    driver.execute_script(script)

# 출력
for i, j, k in zip(img_src_list, no_list, name_list):
    print(j)
    print(k)
    print(i)