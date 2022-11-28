import praw
import random 
from textblob import TextBlob
reddit = praw.Reddit('bot')
submission = random.choice(list(reddit.subreddit('cs40_2022fall').hot(limit=None)))
while True:
    submission.comments.replace_more(limit=None, threshold=0)
    all_comments = submission.comments.list()
    for comment in all_comments:
        print('looking at comment')
        try:
            if 'trump' in comment.body.lower():
                blob = TextBlob(comment.body)
                print(blob.sentiment.polarity)
                if blob.sentiment.polarity < 0:
                    comment.upvote()
                else:
                    comment.downvote()
        except:
            print('this comment was deleted')
    submission = random.choice(list(reddit.subreddit('cs40_2022fall').hot(limit=None)))
            

