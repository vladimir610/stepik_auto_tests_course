from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

path = r'/media/vladimir/MyDisk/работа/my_doc/proekt/ucheba/stepik/selenium/geckodriver'


browser = webdriver.Firefox(executable_path=path)
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text