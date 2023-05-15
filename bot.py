from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

def get_element(driver, xpath):
    wait = WebDriverWait(driver, 100)
    return wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

def reduce_list(liste):
    new_liste = []
    for element in liste:
        if element not in new_liste:
            new_liste.append(element)
    return new_liste

def login(driver):
    driver.get('https://10fastfingers.com/login')
    username = get_element(driver, '//*[@id="UserEmail"]')
    password = get_element(driver, '//*[@id="UserPassword"]')
    username.send_keys('mcy34283@nezid.com')
    password.send_keys('Password')
    anmeldebutton = get_element(driver, '//*[@id="login-form-submit"]')
    anmeldebutton.click()
    time.sleep(2)

driver = 1
driver = webdriver.Chrome()
login(driver)
driver.get('https://10fastfingers.com/advanced-typing-test/german')
list_of_text = []
counter = 0
while True:
    text = get_element(driver, '//*[@id="row1"]')
    text = text.text.split()
    list_of_text.extend(text)
    input_field = get_element(driver, '//*[@id="inputfield"]')
    input_field.send_keys(list_of_text[counter])
    input_field.send_keys(Keys.SPACE)
    time.sleep(random.uniform(0.1, 0.5))
    counter += 1
    list_of_text = reduce_list(list_of_text)

