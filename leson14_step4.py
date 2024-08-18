import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    footer = browser.find_element(By.TAG_NAME, "footer")
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
    x = browser.find_element(By.ID, "input_value").text
    # значение атрибута
    val = calc(x)
    print(val)
    input_val = browser.find_element(By.ID, "answer")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", input_val)
    input_val.send_keys(val)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    
    option2.click()
    
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()