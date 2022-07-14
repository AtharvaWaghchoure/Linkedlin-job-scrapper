import os
from logging import exception
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


#username and password

#---------------------------
USERNAME = ""
PASSWORD = ""
#---------------------------

#Path of the chromedriver  
os.environ['PATH'] += r'.\chromedriver.chromedriver.exe'
driver = webdriver.Chrome()

#get the website
try:
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    driver.implicitly_wait(20)
except exception as e:
    print('Unable to Load the page')

#login functionality
try:
    username = driver.find_element_by_id('username')
    username.send_keys(USERNAME)
    password = driver.find_element_by_id('password')
    password.send_keys(PASSWORD)
    button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
    button.click()
    driver.get('https://www.linkedin.com/jobs/')
    time.sleep(3)
    search_bar = driver.find_element_by_class_name('jobs-search-box__text-input')
    
    search_keyword = search_bar[0]
    search_keyword.send_keys('data engineer')
    
    search_location = search_bar[1]
    search_location.send_keys('maharastra')
    search_location.send_keys(Keys.ENTER)

except exception as e:
    print('Unable to login')


