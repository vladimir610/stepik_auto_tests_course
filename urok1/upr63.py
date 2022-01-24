# -*- coding=utf-8 -*-

from selenium import webdriver
import time
path = r'D:\my_doc\proekt\ucheba\stepik\selenium\geckodriver.exe'
browser = webdriver.Firefox(executable_path=path)
try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
