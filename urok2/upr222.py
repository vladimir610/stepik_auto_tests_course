# -*- coding=utf-8 -*-
#!/usr/bin/env python3

import math
import time
from tkinter import Button

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

    value2 = '#input_value'
    x_element = browser.find_element_by_css_selector(value2)
    y = calc(x_element.text)
    
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 200);")
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element_by_css_selector('.btn-primary')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    time.sleep(20)
    browser.quit()
