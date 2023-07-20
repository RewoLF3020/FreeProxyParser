from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import time


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.add_argument("--disable-blink-features=AutomationControlled")

# disable webdriver

# # for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

try:
    start_time = datetime.datetime.now()
    
    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty")
    # print(driver.window_handles)
    print(f"Currently URL is:{driver.current_url}")
    
    # implicitly_wait отличается тем, что если ресурс загрузиться раньше переданного времени, то работа продолжиться без ожидания оставшегося времени
    # но если нужно сэмулировать поведение пользователя, то time.sleep(random...)
    # time.sleep(5)
    driver.implicitly_wait(5)
    
    items = driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)
    driver.implicitly_wait(5)
    
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    print(f"Currently URL is:{driver.current_url}")
    
    username = driver.find_element(By.CLASS_NAME, "style-seller-info-name-uWwYv")
    print(f"User name is: {username.text}")
    print("#" * 20)
    driver.implicitly_wait(5)
    
    driver.implicitly_wait(5)
    
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(5)
    print(f"Currently URL is:{driver.current_url}")
    
    items[1].click()
    driver.implicitly_wait(5)
    
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    print(f"Currently URL is:{driver.current_url}")
    username = driver.find_element(By.XPATH, "//div[@data-marker='style-seller-info-name-uWwYv']")
    print(f"User name is: {username.text}")
    print("-" * 20)
    
    ad_date = driver.find_element(By.CLASS_NAME, "title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")
    print("-" * 20)
    driver.implicitly_wait(5)
    
    finish_time = datetime.datetime.now()
    spent_time = finish_time - start_time
    print(spent_time)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()