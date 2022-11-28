import praw
import random 
reddit = praw.Reddit('bot')
for i in range(300):
    submission = random.choice(list(reddit.subreddit('liberal').hot(limit=None)))
    reddit.subreddit('cs40_2022fall').submit(submission.title,url=submission.url)
    print(i)
