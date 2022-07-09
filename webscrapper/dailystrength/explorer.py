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





file1 = open('demofile2.txt', 'r')
Lines = file1.readlines()

profiles_ids = set()
 
count = 0
# Strips the newline character
for line in Lines:
    link = line[:-1]
    browser.get(link)
    html = browser.page_source  
    soup = BeautifulSoup(html, features="html.parser")


    # texto, data, info da pessoa
    original_post_p = soup.find_all("div", {"class": "posts__content"})
    original_post = ""
    for p in original_post_p:
        original_post = original_post + p.find('p').text
    
    original_post = original_post.replace('\t', '').replace('\n', '')
    original_post = original_post.strip()

    profile_original = soup.select_one('#main-content > section > div > div.right-sidebar-layout__content > div.right-sidebar-layout__with-border.group-discussion-container > div.group-discussion-container__post > div.newsfeed__item-header > div.newsfeed__title-block > span > span > a')
    profile_link = profile_original.get('href')

    profiles_ids.add(profile_link)

    #print(original_post)
    count += 1

    answer_posts = soup.find_all("div", {"class" : "comments__comment-text"})

    answers = []
    for answer in answer_posts:
        temp = answer.text
        temp = temp.replace('\t', '').replace('\n', '')
        temp = temp.strip()
        answers.append(temp)

    # https://www.dailystrength.org/user/profile/2479161

    #browser.get('https://www.dailystrength.org' + profile_link)
    dates_scrapped = soup.select('.newsfeed__itemtime')
    dates = []
    dates.append(soup.select_one('.newsfeed__item-time').get('datetime'))
    for date in dates_scrapped:
        dates.append(date.get('datetime'))



    for ids in soup.select('#main-content > section > div > div.right-sidebar-layout__content > div.right-sidebar-layout__with-border.group-discussion-container > div.comments > div > div.comments__text-block > div > span > a'):
        profiles_ids.add(ids.get('href'))

    

    
    print(len(dates))
    print(len(profiles_ids))
    print(original_post)
    print(answers)
    print("*******************")
    break


f = open("profiles.txt", "a")



for profile_id in profiles_ids:
    f.write(profile_id)
    f.write('\n')

f.close()
    
    

    
print(count)
browser.quit()
    



