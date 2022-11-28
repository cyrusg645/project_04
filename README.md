# project_04

For this project, I generated comments underneath reddit posts under the username @cgaylord25bot in the form of a madlibs related to tidbits about myself. I wrote it in this form as I wanted to write it in a theme that wasn't about politics but was still connected.

# Favorite Thread

My favorite [thread](https://www.reddit.com/r/cs40_2022fall/comments/z6ml34/a_possibility_for_a_win_in_cured_ballots/) can be seen in the image below. Personally, I like the contrast between the political messages and my more light-hearted messages about learning python. I also like being able to see my bots comment alongside some of my other classmates to see what they are writing their madlibs about. ![Favorite Thread](https://raw.githubusercontent.com/cyrusg645/project_04/main/favorite_thread.png)

# Number of Valid Comments counted from bot.py file
```
len(comments)= 1000
len(top_level_comments)= 735
len(replies)= 265
len(valid_top_level_comments)= 735
len(not_self_replies)= 263
len(valid_replies)= 189
========================================
valid_comments= 924
========================================
```

For my valid comments, I was only able to reach 900 as my number of valid comments started to rapidly decrease over break even when I had it running for most of break. I tried adjusting the rate limit which helped a little but still resulted in lots of my valid comments decreasing which is why I only reached 900. 

# Extra Credit Points:

For extra credit, I was able to get my bot to make 200+ submissions to the CS_40 subreddit using my ```bot_submissions.py``` file giving me 2 points of extra credit. I was able to get my bot to reply to the comments with the largest number of comments instead of random commnets which gives me 2 points as well. Lastly, I created a ```bot_vote.py``` file that utilized the feature Textblob which downvoted posts if they had positive sentiments about Trump and vice versa. Through this, I would get 4 points of extra credit. 

# Overall Points:

Because I finished all tasks on the bot.py file, I'd get 12 points. I'd also get 3 points from creating this repo. Because I only had 900 valid comments, I would get 8 points for the number of valid comments. Lastly, I'd get 8 points from extra credit. This would leave me at 31/30 points for the project. 
