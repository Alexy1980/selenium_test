from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects2.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.ID, "num1").text
    x2 = browser.find_element(By.ID, "num2").text
    y = int(x1) + int(x2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y)) # ищем элемент с текстом = y

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()