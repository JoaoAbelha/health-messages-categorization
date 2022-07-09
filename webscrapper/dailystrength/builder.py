

from ast import Break
from bs4 import BeautifulSoup,Tag, NavigableString
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import itertools

import random

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
# executable_path param is not needed if you updated PATH
browser = webdriver.Firefox(options=options, executable_path='./geckodriver')




records = {
    'Id' : [],
   'ThreadId' : [],
    'MotherId' : [],
    'text' : [],
   'user' : [],
    'date': []
}


THREAD_ID = 1
MSG_ID = 1



def explore_thread(url):

    global THREAD_ID
    global MSG_ID

    browser.get(url)
    html = browser.page_source  
    soup = BeautifulSoup(html, features="html.parser")

    # original message
    initial_question = soup.find("div", {"id": "subject_msg"}).text

    # all users ordered by responses and comments
    username = soup.select('.username')[0]

    response_wrapper = soup.select('.post_list_ctn > .mh_vit_resp_ctn')


    for response in response_wrapper:

        # username, text, date
        print("exploring response")

        u = response.select_one('.username')
        userId =  u.find('a').get('href').split('/')[-1]
        time =  u.find('time').get('data-timestamp')
        #print(username)
        body = response.select_one('.resp_body').text.replace('\t', '').replace('\n', '').strip()

        records['Id'].append(MSG_ID)
        mother_id = MSG_ID
        MSG_ID += 1

        records['ThreadId'].append(THREAD_ID)
        records['MotherId'].append(None)

        records['text'].append(body)
        records['user'].append(userId)
        records['date'].append(time)



        # comments
        comments = response.select_one('.comment_list')

        if comments is None:
            continue

        for comment in comments:
            if isinstance(comment, NavigableString):
                continue
            #print(comment.select_one('.username'))
            comment_body = comment.select_one('.comment_body')
            if comment_body == None:
                continue
            
            username = comment.select_one('.username > a').get('href').split('/')[-1]
            
            date = comment.select_one('.username > time').get('data-timestamp')
            
            records['Id'].append(MSG_ID)
            MSG_ID += 1

            records['ThreadId'].append(THREAD_ID)
            records['MotherId'].append(mother_id)

            records['text'].append(comment_body.text.replace('\t', '').replace('\n', '').strip())
            records['user'].append(username)
            records['date'].append(date)



    THREAD_ID += 1


file1 = open('QA_medhelp.txt', 'r')
Lines = file1.readlines()

total_links = []

print("Start building database...")
for line in Lines:
    link = line[:-1]
    total_links.append(link)


selected_threads = random.sample(total_links, 250)


for x in selected_threads:
    try:
        explore_thread('https://www.medhelp.org/' + x)
    except:
        print('problem in ' + x)


browser.quit()

import pandas as pd

df = pd.DataFrame(records)

df.to_csv('out.csv', index=False)


f = open('explored_threads.txt', 'a')

for l in selected_threads:
    f.write(l)
    f.write('\n')

f.close()
 


