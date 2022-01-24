# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def write_regist(elems):
    i = len(elems) - 1
    while i != -1:
        elems[i].send_keys("Мой ответ")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        #assert "Congratulations! You have successfully registered!" != welcome_text
        time.sleep(3)
        i -= 1




if __name__ == "__main__":
    # Путь к файлу драйвера
    path = r'D:\my_doc\proekt\ucheba\stepik\selenium\urok1\chromedriver.exe'

    link = [
        "http://suninjuly.github.io/registration1.html", 
        "http://suninjuly.github.io/registration2.html"
        ]                                               # Ссылки

    sel = [
        'input.form-control.first[required]', 
        'input.form-control.second[required]', 
        'input.form-control.third[required]'
        ]                                       # Обезательные елементы
    sel_not = 'input:not(input[required]) '     # Не обезательные елементы
    try:
        for i in link:
            browser = webdriver.Chrome(executable_path=path)
            browser.get(i)
            elements_not = browser.find_elements_by_tag_name(sel_not)
            try:
                elements = [browser.find_element_by_tag_name(i) for i in sel]
            except NoSuchElementException:
                print('-*-' * 20)
                print('NoSuchElementException')
                print(f'Ошибка: Не найден элимент интерфейса')
                print('-*-' * 20)
                browser.quit()
            
            write_regist(elements_not) 
            write_regist(elements)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            print('-*-' * 20)
            print(f'Регистрация прохла успешно! \n{welcome_text}')
            print('-*-' * 20)
            browser.close()

    finally:
        # успеваем скопировать код за 10 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
