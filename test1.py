from selenium import webdriver 
from selenium.webdriver.common.by import By 

browser=webdriver.Chrome() 
browser.get(' http://localhost:3000/login') 

login=browser.find_element(by=By.ID, value='login') 
login.send_keys(' Admin090909') 

password=browser.find_element(by=By.ID, value='password') 
password.send_keys('12345') 

button=browser.find_element(by=By.CSS_SELECTOR, value='#avtorizbtn') 
button.click()

