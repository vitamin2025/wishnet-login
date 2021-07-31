import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


a = '{{variable_username}}'
b = '{{variable_passwword}}'



driver = webdriver.Chrome()
driver.get("http://192.168.182.201:9086/Rowb1/WISHN/Login.jsp")

username = driver.find_element_by_name("Username")
password = driver.find_element_by_name("Password")
username.send_keys(a)
password.send_keys(b)
btn = driver.find_element_by_id("submit_btn")
btn.click()

time.sleep(3)
time.close()