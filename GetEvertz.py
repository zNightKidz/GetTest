from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')


url = 'https://172.22.2.123'
driver.get(url)

#登陆

driver.find_element_by_name('user').clear()
driver.find_element_by_name('user').send_keys('admin')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('admin')
driver.find_element_by_name('SubmitPassword').click()
time.sleep(3)

#切流

#driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/li[9]/a").click()
driver.find_element_by_link_text('Video Input Control').click()
time.sleep(3)
driver.find_element_by_id('220.0.0@s').clear()
driver.find_element_by_id('220.0.0@s').send_keys('226.0.0.7')
driver.find_element_by_id('Applybutton').click()
