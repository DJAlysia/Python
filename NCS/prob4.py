from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.instagram.com/'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

id = "lottie_eve@naver.com"
pw = "doyeon96^^"


driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(id)
password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
password.send_keys(pw)
password.submit()

    
time.sleep(5)
driver.find_element(By.XPATH, "//div[contains(text(), '나중에 하기')]").click()
    
    
time.sleep(3)

driver.find_element(By.XPATH, "//button[contains(text(), '나중에 하기')]").click()
url_list = []
now = 0
while True:
    now = len(driver.find_elements(By.CSS_SELECTOR, "article"))

    print(now)

    if now >= 10:
        break

    photos = driver.find_elements(By.CSS_SELECTOR, "._aagv")

    for photo in photos:
        url = photo.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        url_list.append(url)
        
    script = "document.body.scrollIntoView(false);"
    driver.execute_script(script)

print(url_list)