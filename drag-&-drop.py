from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path='C:\\Users\\Sebastian\\Documents\\Projects\\web-browsing-automation\\geckodriver.exe')

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element_by_xpath('//*[@id="box6"]')
destination = driver.find_element_by_xpath('//*[@id="box106"]')

action = ActionChains(driver)
action.drag_and_drop(source, destination).perform()