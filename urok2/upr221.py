# -*- coding=utf-8 -*-
#!/usr/bin/env python3

import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def prnt(lst:list):
    for i, vol in enumerate(lst):
        print(i, vol)


link = "http://suninjuly.github.io/execute_script.html"
#path = r'D:\my_doc\proekt\ucheba\stepik\selenium\urok1\chromedriver.exe'
path = r'/media/vladimir/MyDisk/работа/my_doc/proekt/ucheba/stepik/selenium/geckodriver'
fox = r'/usr/bin/firefox'

browser = webdriver.Firefox(executable_path=path, firefox_binary=fox)
#browser = webdriver.Chrome(executable_path=path)

try:
    browser.get(link)
    value2 = 'span.nowrap#input_value'
    x_element = browser.find_element_by_css_selector(value2)
    x = x_element.text
    y = calc(x)

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    button = browser.find_element_by_css_selector('button.btn-default')
    button.click()


finally:
    time.sleep(20)
    browser.quit()
