from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    fname = browser.find_element(By.CSS_SELECTOR, 'div[class="form-group first_class"] input[class ="form-control first"]')
    fname.send_keys("Ivan")
    lname = browser.find_element(By.CSS_SELECTOR, 'div[class="form-group second_class"] input[class ="form-control second"]')
    lname.send_keys("Ivanov")
    mail = browser.find_element(By.CSS_SELECTOR, 'div[class="form-group third_class"] input[class ="form-control third"]')
    mail.send_keys("ivan1986@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()