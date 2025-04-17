import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# запускать python -m pytest test_pytest_style.py

browser = webdriver.Chrome()


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()

if __name__ == "__main__":
    pytest.main()