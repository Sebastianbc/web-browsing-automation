from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Web page that uses AJAX, waits are suitable for these scenarios
url = 'https://www.google.com/intl/es/earth/'
driver = webdriver.Firefox(executable_path='./geckodriver.exe')
driver.get(url)

# Explicit wait
wait = WebDriverWait(driver, 10)
# Implicit wait, wait until a condition (the element appears in the web page)
earth_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
earth_button.click()