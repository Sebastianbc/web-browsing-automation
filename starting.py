from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:\\Users\\Sebastian\\Documents\\Projects\\web-browsing-automation\\geckodriver.exe')

driver.get('https://www.w3schools.com/sql/exercise.asp')
textbox = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div[4]/div[5]/pre[1]/input')
textbox.send_keys('select')
submit_buttom = driver.find_element_by_xpath('//*[@id="answerbutton"]')
submit_buttom.click()