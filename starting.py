from selenium import webdriver

# Initialize webdriver object with geckodriver.exe file downloaded previously
driver = webdriver.Firefox(executable_path='C:\\Users\\Sebastian\\Documents\\Projects\\web-browsing-automation\\geckodriver.exe')

# Open target web page
driver.get('https://www.w3schools.com/sql/exercise.asp')
# Find element
textbox = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div[4]/div[5]/pre[1]/input')
# Send value to element
textbox.send_keys('select')
# Find another element
submit_buttom = driver.find_element_by_xpath('//*[@id="answerbutton"]')
# Perform click action on element
submit_buttom.click()