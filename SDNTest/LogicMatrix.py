from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()

# 使用headless无界面浏览器模式
#增加无界面选项
#options.add_argument('--headless')
#如果不加这个选项，有时定位会出现问题
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(options=options)

'''
#登陆163企业邮箱
# 启动浏览器，获取网页源代码
mainUrl = "https://qiye.163.com/login/"
browser.get(mainUrl)
sleep(5)
acount = browser.find_element_by_id("accname")
acount.clear()
acount.send_keys("zhangjinbo@ndtchina.com")
pwd = browser.find_element_by_id("accpwd")
pwd.clear()
pwd.send_keys("zhjinbo2018!")
sleep(3)
#loginbutton = browser.find_element_by_class_name("w-button w-button-account js-loginbtn")
loginbutton = browser.find_element_by_xpath("/html/body/section/div/div[2]/div[2]/form[1]/div[5]/button")
loginbutton.click()
sleep(5)
browser.close()
'''

#登陆豆瓣
mainurl = "https://www.douban.com/"
doubanuser = "1123525567@qq.com"
doubanpwd = "1175233452zjb"
browser.get(mainurl)
sleep(3)
#切换到iframe

iframe = browser.find_elements_by_tag_name("iframe")[0]
browser.switch_to.frame(iframe)
sleep(1)
denglu = browser.find_element_by_class_name("account-tab-account")
ActionChains(browser).click(denglu).perform()
sleep(3)
myname = browser.find_element_by_id("username")
myname.clear()
myname.send_keys(doubanuser)

sleep(1)
sss = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[4]/div/input")
sss.clear()
sss.send_keys(doubanpwd)
sleep(1)
ActionChains(browser).click(browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[5]/a")).perform()
sleep(1)
#切换iframe
browser.switch_to.frame("tcaptcha_iframe")

pintu = browser.find_element_by_id("tcaptcha_drag_thumb")
#pintu = browser.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]")
action = ActionChains(browser)
action.click_and_hold(pintu)
action.move_by_offset(213,0)
action.perform()
sleep(1)


