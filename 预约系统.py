from selenium import webdriver 
import time


my_driver_path = "C:/Users/Administrator/AppData/Local/Programs/Python/chromedriver.exe"
driver = webdriver.Chrome(executable_path=my_driver_path)

url = 'http://140.143.51.156:8080/user/gallery.jsp'
driver.get(url)

#登陆
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('sunshixin')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_id('dosubmit').click()
time.sleep(3)

#进入演播室预约
driver.find_element_by_className('link-stutio cur').click()
