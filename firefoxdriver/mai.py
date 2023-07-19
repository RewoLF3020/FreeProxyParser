from selenium import webdriver
import time


url = "https://www.site.com/"
driver = webdriver.Firefox(executable_path="/home/vlad/projects/Selenium/firefoxdriver/geckodriver")

try:
    driver.get(url=url)
    driver.save_screenshot("vk.png")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()