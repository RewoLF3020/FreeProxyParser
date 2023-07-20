from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import inst_username, inst_password
import time


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
options.headless = True

service = Service(
    executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('https://www.instagram.com/')
    time.sleep(5)

    print("Passing authentication...")
    username = driver.find_element(By.NAME, 'username')
    username.clear()
    username.send_keys(inst_username)
    time.sleep(2)

    password = driver.find_element(By.NAME, 'password')
    password.clear()
    password.send_keys(inst_password)
    time.sleep(2)

    password.send_keys(Keys.ENTER)
    time.sleep(10)

    # profile_button = driver.find_element(By.CSS_SELECTOR, 'a.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft').click()
    # time.sleep(5)
    
    print("Going to the post...")
    video_post = driver.get("https://www.instagram.com/p/CuCtfX_OJWj/")
    time.sleep(5)
    
    print("Unmuting audio...")
    unmute_audio = driver.find_element(By.XPATH, '''/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]''')
    unmute_audio.click()
    time.sleep(5)
    print("Finish watching the video...")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
