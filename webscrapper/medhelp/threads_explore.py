from ast import Break
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import datetime

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
# executable_path param is not needed if you updated PATH
browser = webdriver.Firefox(options=options, executable_path='./geckodriver')


f = open('novo_boy.txt', 'w')


file1 = open('medhelp_list.txt', 'r')
Lines = file1.readlines()


def explore_number(url):

  current_page = 1
  max_page = 500
 
  browser.get(url)

  # we get five per page, so the number of threads we get is max_page * 5 * number of communities
  while current_page <= max_page:
    current_page +=1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    import time
    time.sleep(1)


   
  html = browser.page_source  
  soup = BeautifulSoup(html, features="html.parser")

  subj_links = soup.select('.subj_title > a')

  for link in subj_links:
      f.write(link.get('href'))
      f.write('\n')



counter = 0
for line in Lines:
    counter +=1
    link = line[:-1]
    explore_number(link)
    print(link, " done " + str(counter) + "/" + str(len(Lines)))

f.close()    
browser.quit()

