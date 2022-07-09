from calendar import month
import pandas as pd
import datetime as dt
import os

import praw
from psaw import PushshiftAPI
# to use PSAW
api = PushshiftAPI()
# to use PRAW
reddit = praw.Reddit(
    user_agent="MyBot/0.0.1",
    client_id="ZlfxzjyaLsA9B4jiVK01BA",
    client_secret="_i_HGBtmTqfRiafuV_zmQs0WrCvk7w",
    username="Bee31099",
    password="boris1999",
)


subreddits = ['depression']
start_year = 2022
end_year = 2022
month_start = 1
month_end = 3
# directory on which to store the data
basecorpus = './my-dataset/'


import time
def log_action(action):
    print(action)
    return


### BLOCK 1 ###

for year in range(start_year, end_year+1):
  for mon in range(month_start, month_end + 1):
    action = "[Year] " + str(year) + " [month] " + str(mon)
    log_action(action)

    dirpath = basecorpus + str(year) + "-" + str(mon)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    # timestamps that define window of posts
    ts_after = int(dt.datetime(year, mon, 1).timestamp())
    ts_before = int(dt.datetime(year+1, mon + 1, 1).timestamp())

### BLOCK 2 ###

    for subreddit in subreddits:
        start_time = time.time()

        action = "\t[Subreddit] " + subreddit
        log_action(action)

        subredditdirpath = dirpath + '/' + subreddit
        if os.path.exists(subredditdirpath):
            continue
        else:
            os.makedirs(subredditdirpath)

        submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'
        
### BLOCK 3 ###

        submissions_dict = {
            "comment_id" : [],
            "comment_link_id" : [],
            "comment_parent_id" : [],
            #"score" : [],
            #"num_comments": [],
            "created_utc" : [],
            "comment_body" : [],
        }

        submission_comments_dict = {
            "comment_id" : [],
            "comment_parent_id" : [],
            "comment_body" : [],
            "comment_link_id" : [],
            "created_utc": [],
        }

### BLOCK 4 ###

        # use PSAW only to get id of submissions in time interval
        gen = api.search_submissions(
            after=ts_after,
            before=ts_before,
            filter=['id'],
            subreddit=subreddit,
            limit=100
        )

### BLOCK 5 ###

        # use PRAW to get actual info and traverse comment tree
        for submission_psaw in gen:
            # use psaw here
            submission_id = submission_psaw.d_['id']
            # use praw from now on
            submission_praw = reddit.submission(id=submission_id)

            submissions_dict["comment_id"].append(submission_praw.id)
            submissions_dict['comment_parent_id'].append(None)
            submissions_dict["comment_link_id"].append(submission_praw.url)
            #submissions_dict["title"].append(submission_praw.title)
            #submissions_dict["score"].append(submission_praw.score)
            #submissions_dict["num_comments"].append(submission_praw.num_comments)
            submissions_dict["created_utc"].append(submission_praw.created_utc)
            submissions_dict["comment_body"].append(submission_praw.selftext.replace('\t', '').replace('\n', '').strip())

### BLOCK 6 ###

            submission_comments_csv_path = str(year) + '-' + subreddit + '-submission_' + '-comments.csv'
        

### BLOCK 7 ###

            # extend the comment tree all the way
            submission_praw.comments.replace_more(limit=None)



            # for each comment in flattened comment tree
            for comment in submission_praw.comments.list():
                submission_comments_dict['created_utc'].append(comment.created_utc)
                submission_comments_dict["comment_id"].append(comment.id)
                submission_comments_dict["comment_parent_id"].append(comment.parent_id)
                submission_comments_dict["comment_body"].append(comment.body.replace('\t', '').replace('\n', '').strip())
                submission_comments_dict["comment_link_id"].append(comment.link_id)

            # for each submission save separate csv comment file


        for x in submissions_dict:
            print(x, len(submissions_dict[x]))

        pd.DataFrame(submission_comments_dict).to_csv(subredditdirpath + '/'  + str(year) + "-" + str(mon) + submission_comments_csv_path ,
                                                          index=False)

### BLOCK 8 ###
        # single csv file with all submissions
        pd.DataFrame(submissions_dict).to_csv(subredditdirpath + '/' + submissions_csv_path,
                                              index=False)


        action = f"\t\t[Info] Found submissions: {pd.DataFrame(submissions_dict).shape[0]}"
        log_action(action)

        action = f"\t\t[Info] Elapsed time: {time.time() - start_time: .2f}s"
        log_action(action)