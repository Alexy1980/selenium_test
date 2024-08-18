from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который заполняет обязательные поля
    required_elements = browser.find_elements_by_css_selector('input[required]')
    for element in required_elements:
        element.send_keys('required')

    # необязательные поля
    address = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your address:')]")
    address.send_keys("Moscow")
    phone = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your phone:')]")
    phone.send_keys("+7899677566")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
   
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    
    time.sleep(5)
    
    browser.quit()