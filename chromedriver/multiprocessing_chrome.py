from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from multiprocessing import Pool
import random
import time


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.add_argument("--disable-blink-features=AutomationControlled")

urls_list = ["https://github.com/", " https://www.ted.com/ru", "https://www.coursera.org/", "https://www.reddit.com/", " https://medium.com/"]


# def get_data(url):
#     try:
#         service = Service(executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver")
#         driver = webdriver.Chrome(service=service, options=options)
#         driver.get(url=url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")

#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()


# if __name__ == '__main__':
#     p = Pool(processes=1)
#     p.map(get_data, urls_list)


def get_data(url):
    try:
        service = Service(executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url=url)
        time.sleep(5)
        # driver.find_element(By.CLASS_NAME, "lazyload-wrapper").find_element(By.CLASS_NAME, "item-video-container").click()
        time.sleep(random.randrange(3, 10))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)