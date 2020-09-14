from selenium import webdriver
import time

# my_driver_path = ''
# driver = webdriver.Chrome(executable_path=my_driver_path)
driver = webdriver.Chrome()
url = 'https://qiye.163.com/login/'
driver.get(url)
time.sleep(1)

#切换到密码登陆
driver.find_element_by_id('lbNormal').click()
#登陆
driver.find_element_by_id('accname').clear()
driver.find_element_by_id('accname').send_keys('zhangjinbo@ndtchina.com')
driver.find_element_by_id('accpwd').clear()
driver.find_element_by_id('accpwd').send_keys('zhjinbo2018!')
driver.find_element_by_class_name('loginbtn').click()
time.sleep(1)

#查看收件箱
driver.find_element_by_id('_mail_component_38_38').click()
time.sleep(1)


