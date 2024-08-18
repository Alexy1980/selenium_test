from selenium import webdriver

# Указание пути к ChromeDriver
chrome_driver_path = 'C:/chromedriver_win32/chromedriver.exe'

# Запуск Chrome с использованием Selenium
driver = webdriver.Chrome(chrome_driver_path)

# Открытие веб-страницы
driver.get('http://yandex.ru')

# Закрытие браузера
driver.quit()