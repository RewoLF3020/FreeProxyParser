from selenium import webdriver
# from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from config import login, password
from px_scrap import get_proxy


url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

user_agents_list = [
    "hello",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
    "lallalala",
]

options = webdriver.ChromeOptions()

useragent = UserAgent()

# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.random}")
# options.add_argument("--proxy-server=116.111.219.235:23775")

#if you want to use proxy with auth without bind IP address
# proxy_options = {
    # "proxy": {
        # "https": f"{login}:{password}@116.111.219.235:23775"
    # }
# }

# driver = webdriver.Chrome(
    # executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver",
    # seleniumwire_options=proxy_options
# )


# driver = webdriver.Chrome(
    # executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver",
    # options=options
# )

""" try:
    # driver.get(url=url)
    # time.sleep(10)
    driver.get("https://2ip.ru")
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit() """


# Откройте сайт Google в браузере и авторизуйтесь в свою учетную запись Google.
# Откройте инструменты разработчика в вашем браузере (обычно это можно сделать, нажав клавиши F12).
# Перейдите на вкладку "Application" (или "Storage" в Firefox).
# В левой панели выберите пункт "Cookies" и затем выберите домен ".google.com".
# Найдите cookie с именем "SID" и скопируйте его значение.
# SID обычно имеет срок действия и может периодически меняться.
# Поэтому, если вы хотите использовать SID в тестах, вам может потребоваться обновлять его регулярно.
cookies = {
    'name': 'SID',
    'value': 'YgjWHOQGEJvOtIEyH29MoAWE-1emTwuQlXagkdBcDV8cVR-a4Dj7jBdwOVJ6a9vUxSnaMA.',
    'domain': '.google.com', 
    'path': '/',
    'httpOnly': True,
    'secure': True,
    'expires': None
}


while True:
    PROXY = get_proxy(scrap=True)
    options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(options=options, executable_path="/home/vlad/projects/Selenium/chromedriver/chromedriver")
    try:
        driver.get('https://google.com')
        # driver.add_cookie(cookies)
    except Exception as ex:
        print(ex)
        # print('Captcha!')