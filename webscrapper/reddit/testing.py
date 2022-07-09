import praw
from praw.models import MoreComments


reddit = praw.Reddit(
    user_agent="MyBot/0.0.1",
    client_id="ZlfxzjyaLsA9B4jiVK01BA",
    client_secret="_i_HGBtmTqfRiafuV_zmQs0WrCvk7w",
    username="Bee31099",
    password="boris1999",
)


url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(id="taofpm")

print(submission.selftext)


submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)
    print("************")