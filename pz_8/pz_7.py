from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mongo_base = client.unsplash300524

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)

driver.get("https://e.mail.ru/inbox/")
# процесс ввода логина и пароля скрыт в целях безопасности!
time.sleep(5)

# print()
letters = driver.find_elements(By.CLASS_NAME, "llc") # 100
# url = letters[0].find_element(By.XPATH,"./a").get_attribute('href')
count_letter = 0
try:
    url = letters[0].get_attribute('href')
    driver.get(url)
except:
    print("break 1")
while True:
    try:
        time.sleep(5)
        name = driver.find_element(By.CLASS_NAME, "thread__subject-line").text
        sender = driver.find_element(By.CLASS_NAME, "letter-contact").text
        let_date = driver.find_element(By.CLASS_NAME, "letter__date").text
        print(name, sender, let_date)

        # TODO: save to database
        count_letter += 1
        item_letter = {}
        item_letter["name"] = name
        item_letter["sender"] = sender
        item_letter["let_date"] = let_date
        collection = mongo_base["letters"]
        collection.insert_one(item_letter)

        # ограничение на кол-во писем, если его убираем, то скачиваются все письма!
        if count_letter == 25:
            break

        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL)
        actions.perform()
        # actions.move_to_element(url).click()
        # url.click()
        # actions.perform()
    except:
        print("break")
        break

driver.quit()