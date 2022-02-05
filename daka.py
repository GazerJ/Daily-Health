#! /usr/bin/python3
#coding=utf-8
#@author: Gazer
from selenium import webdriver
import time


opt = webdriver.ChromeOptions()                 #创建浏览器
opt.add_experimental_option('excludeSwitches',['enable-automation'])
opt.add_argument("--no-sandbox")
opt.add_argument("window-size=1920x1080")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--disable-gpu")
opt.add_argument("--blink-settings=imagesEnable=false")
opt.add_argument("--headless")                         #无窗口模式
driver = webdriver.Chrome(options=opt)#创建浏览器对象
try:
	time.sleep(3)
	driver.get("https://xmuxg.xmu.edu.cn/login")
	driver.refresh()
	time.sleep(3)
	#登录
	driver.find_elements_by_css_selector('.btn.primary-btn')[2].click()
	driver.find_elements_by_id('username')[0].send_keys("** 学号**")
	driver.find_elements_by_id('password')[0].send_keys("**密码**")
	driver.find_elements_by_css_selector(".auth_login_btn.primary.full_width")[0].click()
	#跳转到打卡页面
	time.sleep(3)
	driver.get("https://xmuxg.xmu.edu.cn/app/214")
	time.sleep(3)
	driver.refresh()
	time.sleep(3)
	driver.find_elements_by_css_selector('.tab')[1].click()
	time.sleep(3)
	driver.find_elements_by_css_selector('.form-control.dropdown-toggle')[16].click()
	driver.find_elements_by_css_selector('.btn-block')[-1].click()
	driver.find_elements_by_css_selector('.form-save.position-absolute')[0].click()
	driver.switch_to.alert.accept()
	print("sccessful  ",end='/')
	
except:
        print("error") 
        pass
driver.close()

