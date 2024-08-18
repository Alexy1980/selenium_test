from selenium import webdriver
from selenium.webdriver.common.by import By
DRIVER_PATH = 'C:/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.google.com/maps/search/cafe+in+new+york/')

results_title = []
results_ots = []
elems_title = driver.find_elements(By.XPATH, "//div[@class='NrDZNb']")
elems_ots = driver.find_elements(By.XPATH, "//span[@class='UY7F9']")

for elem in elems_title:
    title = elem.find_element(By.CSS_SELECTOR, "div.fontHeadlineSmall")
    
    results_title.append(str(title.text))

for elem in elems_ots:   
    results_ots.append(str(elem.text))

res = list(zip(results_title, results_ots))

driver.close()
print(res)