# -*- coding=utf-8 -*-
#!/usr/bin/env python3


from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def prnt(lst:list):
    for i, vol in enumerate(lst):
        print(i, vol)


link = "http://suninjuly.github.io/get_attribute.html"
#path = r'D:\my_doc\proekt\ucheba\stepik\selenium\urok1\chromedriver.exe'
path = r'/media/vladimir/MyDisk/работа/my_doc/proekt/ucheba/stepik/selenium/geckodriver'
fox = r'/usr/bin/firefox'
browser = webdriver.Firefox(executable_path=path, firefox_binary=fox)

try:
    #browser = webdriver.Chrome(executable_path=path)
    browser.get(link)


    value2 = '#treasure'
    x_element = browser.find_element_by_css_selector(value2)
    x = x_element.get_attribute('valuex')
    y = calc(x)

    value1 = 'input.form-control'
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(str(y))

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    button = browser.find_element_by_css_selector('.btn-default')
    button.click()

finally:
    time.sleep(20)
    browser.quit()
