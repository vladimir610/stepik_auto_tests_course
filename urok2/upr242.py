# -*- coding=utf-8 -*-
#!/usr/bin/env python3

import os
import math
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = 'http://suninjuly.github.io/explicit_wait2.html'
# path = r'E:\работа\my_doc\proekt\ucheba\stepik\selenium\chromedriver.exe'
# path = r'/media/vladimir/MyDisk/работа/my_doc/proekt/ucheba/stepik/selenium/geckodriver'
path = r'D:\my_doc\proekt\ucheba\stepik\selenium\geckodriver.exe'


browser = webdriver.Firefox(executable_path=path)
# browser = webdriver.Chrome(executable_path=path)
current_dir = os.path.abspath(os.path.dirname(__file__))


try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

    button = browser.find_element_by_css_selector('#book')
    button.click()

    # button = browser.find_element_by_css_selector('.trollface.btn-primary')
    # button.click()


    x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
    y = calc(x_element.text)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button = browser.find_element_by_css_selector('#solve')
    button.click()

finally:
    time.sleep(20)
    browser.quit()
