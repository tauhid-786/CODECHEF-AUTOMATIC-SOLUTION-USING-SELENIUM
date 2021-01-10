#importing library
from selenium import webdriver 
from getpass import getpass
import time
# making an object of webdriver
browser=webdriver.Chrome("C:/Users/hp/Desktop/chromedriver.exe")
#searching required site
browser.get("https:/codechef.com")
username_element=browser.find_element_by_id("edit-name")
print("please enter your username")
username=input()
username_element.send_keys(username)
password_element=browser.find_element_by_id("edit-pass")
# from getpass import getpass
print("please enter your password")
# password_element.send_keys(getpass("enter your password"))
password=input()
password_element.send_keys(password)
button1=browser.find_element_by_id("edit-submit")
time.sleep(10)
button1.click()
print("enter your problem name")
prblm=input()
browser.get("https://www.codechef.com/submit/"+prblm)
id_arg='edit_area_toggle_checkbox_edit-program'
# x_arg = '/html/body/center/center/table/tbody/tr/td/div/div/div/div[2]/form[2]/div/div[2]/div[1]/div/span/div/input'
button2=browser.find_element_by_xpath(id_arg)
# button=wait.until(EC.presence_of_element_located(( 
    # By.XPATH, x_arg))) 
# button.click()
time.sleep(20)
button2.click()
with open ("solution.cpp","r") as f:
    code=f.read();
# time.sleep(10)
code_element=browser.find_element_by_id('edit-program')
code_element.send_keys(code)
time.sleep(10)
button3=browser.find_element_by_id("edit-submit-1")
time.sleep(10)
button3.click()
