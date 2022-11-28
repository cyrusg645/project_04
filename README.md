# project_04

For this project, I generated comments underneath reddit posts under the username @cgaylord25bot in the form of a madlibs related to tidbits about myself. 

# Favorite Thread

The image below is probably my favorite thread as I 

# Number of Valid Comments counted from bot.py file
```
cyrus@Cyruss-MacBook-Air-2 cyrusg645.github.io % /usr/local/bin/python3 /Users/cyrus/Documents/GitHub/cyrusg645.github.io/bot_counter.py --username=cgaylord25bot
len(comments)= 1000
len(top_level_comments)= 391
len(replies)= 609
deleted comments
deleted comments
len(valid_top_level_comments)= 389
len(not_self_replies)= 588
len(valid_replies)= 316
========================================
valid_comments= 705
```

For my valid comments, I was only able to reach 700 as my number of valid comments started to rapidly decrease over break even when I had it running for most of break. I tried adjusting the rate limit which helped a little but still resulted in lots of my valid comments decreasing which is why I only reached 700. 

# Extra Credit Points:

For extra credit, I was able to get my bot to make 200+ submissions to the CS_40 subreddit using my ```bot_submissions.py``` file giving me 2 points of extra credit. I was able to get my bot to reply to the comments with the largest number of comments which gives me 2 points as well. Lastly, I created a ```bot_vote.py``` file that utilized the feature Textblob which downvoted posts if they had positive sentiments about Trump and vice versa. Through this, I would get 4 points of extra credit. 

# Overall Points:

Because I finished all tasks on the bot.py file, I'd get 12 points. I'd also get 3 points from creating this repo. Because I only had 700 valid comments, I would get 4 points for the number of valid comments. Lastly, I'd get 8 points from extra credit. This would leave me at 27/30 points for the project. 
