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

# it loads 15 at a time
nr_pages = 2


url_base = 'https://www.dailystrength.org/group/anxiety'
browser.get(url_base)
#html = browser.page_source  
#soup = BeautifulSoup(html, features="html.parser")


for i in range(nr_pages):
    #load_more_btn = soup.find("button", {"id": "load-more-discussions"})
    #old_value = browser.find_element_by_id('load-more-discussions').text 
    #btn = browser.find_element_by_css_selector('#load-more-discussions')
    #browser.execute_script("arguments[0].click();", btn)

    elem2 = WebDriverWait(browser, 20).until(ec.text_to_be_present_in_element((By.ID, "load-more-discussions"), "SHOW MORE"))


    #browser.find_element_by_css_selector('#load-more-discussions').click()


    btn = browser.find_element_by_css_selector('#load-more-discussions')
    print(btn)
    browser.execute_script("arguments[0].click();", btn)

    elem2 = WebDriverWait(browser, 20).until(ec.text_to_be_present_in_element((By.ID, "load-more-discussions"), "LOADING...")) 

    

    print("next")


    
html = browser.page_source  
soup = BeautifulSoup(html, features="html.parser")

counter = 0
f = open("demofile2.txt", "a")

for element in soup.select('#main-content > section > div.right-sidebar-layout__container > div.right-sidebar-layout__content > div > div.newsfeed > ul > li > div.newsfeed__item-header > div.newsfeed__btns > a'):
    link = element.get('href')
    # remove the last #reply
    remove = "#reply"
    link = link[:-len(remove)]
    counter = counter + 1
    link_to_explore = 'https://www.dailystrength.org' + link
    f.write(link_to_explore)
    f.write('\n')


    print("|" + link_to_explore + "|")

f.close()

browser.quit()

