# -*- coding=utf-8 -*-
#!/usr/bin/env python3

import os
import math
import time


from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def prnt(lst:list):
    for i, vol in enumerate(lst):
        print(i, vol)


link = "http://suninjuly.github.io/file_input.html"
#path = r'D:\my_doc\proekt\ucheba\stepik\selenium\urok1\chromedriver.exe'
path = r'/media/vladimir/MyDisk/работа/my_doc/proekt/ucheba/stepik/selenium/geckodriver'
fox = r'/usr/bin/firefox'

browser = webdriver.Firefox(executable_path=path)
#browser = webdriver.Chrome(executable_path=path)
current_dir = os.path.abspath(os.path.dirname(__file__))     
file_path = os.path.join(current_dir, 'file.txt') 

try:
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')
    prnt(elements)
    for i, element in enumerate(elements):
        if i == 3:
            element = browser.find_element_by_css_selector('input#file')
            element.send_keys(file_path)
        else:
            element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()
finally:
    time.sleep(60)
    #browser.quit()
