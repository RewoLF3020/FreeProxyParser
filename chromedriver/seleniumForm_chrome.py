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

# If you are still using Selenium v3.x then you shouldn't use the Service() and in that case the key executable_path is relevant. 
# In that case the lines of code will be: driver = webdriver.Chrome(executable_path=...
# Else, if you are using selenium4 then you have to use Service() and in that case the key executable_path is no more relevant. 
# So you need to change the line of code:
service = Service(executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver")

driver = webdriver.Chrome(
    service=service,
    options=options
)

try:
    driver.get("https://instagram.com/")
    wait = WebDriverWait(driver=driver, timeout=5)
    
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    username_input.clear()
    username_input.send_keys(inst_username)
    password_input.send_keys(inst_password)
    time.sleep(3)
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    # password_input.send_keys(Keys.ENTER)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()