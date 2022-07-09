from lib2to3.pgen2 import driver
from re import L
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
# executable_path param is not needed if you updated PATH
browser = webdriver.Firefox(options=options, executable_path='./geckodriver')

base_url = 'https://www.dailystrength.org'


file1 = open('profiles.txt', 'r')
Lines = file1.readlines()


for line in Lines:
    link = line[:-1]
    print(base_url + link)

    browser.get(base_url + link)
    html = browser.page_source  
    soup = BeautifulSoup(html, features="html.parser")
    age = - 1
    try: 
        age = soup.select_one('#main-content > div.right-sidebar-layout__container > div.right-sidebar-layout__content > div > div > div.profile-body-cnt__aboutme > div > div').text
        print(age)
    except:
        print("exception for " + link)

browser.quit()
    

