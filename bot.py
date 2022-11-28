import praw
import random
import datetime
import argparse
import time

madlibs = [
    "My favorite movie is [MOVIE]. [EVERYONE] should watch it because it is [FUNNY]. It was recommended to me by my [DAD].",
    "I was born in the [UNITED STATES OF AMERICA]. I wish I could have been born in [SWITZERLAND]. I do really appreciate the [SCENARY] here though.",
    "I like to [SKI]. It is super [FUN] because it involes lots of [THRILLS]. I wish I could do it [ALL THE TIME].",
    "I am very [SOCIAL]. I would also say that I enjoy [SPENDING TIME ON MY OWN]. I wonder if other people are the [SAME]",
    "My favorite language is [PYTHON]. However, it has been hard to [LEARN]. I will [IMPROVE] over time.",
    "I am scared of [ANIMALS]. I have been scared of them since I was [AGE]. Hopefully, I will [OVERCOME] this fear.",
    #"I [LOVE] [PYTHON2]... you [LOVE] [PYTHON2]... we all [LOVE] [PYTHON2]!!!",
    ]

replacements = {
    'MOVIE' : ['The Godfather', 'Kill Bill', 'Star Wars', 'Batman Begins', 'Monsters Inc'],
    'EVERYONE' : ['Everyone', 'All people', 'Every single person I know', 'Tons of people', 'Everyone on the planet'],
    'FUNNY' : ['funny', 'hilarious', 'comical', 'hysterical ', 'a great movie'],
    'DAD' : ['dad', 'mom', 'brother', 'sister', 'grandpa'],
    'UNITED STATES OF AMERICA' : ['United States of America', 'United States', 'US', 'USA', 'America'],
    'SWITZERLAND' : ['Switzerland', 'England', 'Canada', 'Japan', 'France'],
    'SCENARY' : ['scenary', 'people', 'food', 'history', 'culture'],
    'SKI' : ['ski', 'skateboard', 'surf', 'swim', 'dance'],
    'FUN' : ['fun', 'enjoyable', 'relaxing', 'engaging', 'exciting'],
    'THRILLS' : ['thrills', 'exercise', 'adrenaline', 'excitement', 'hard work'],
    'ALL THE TIME' : ['all the time', 'all day', 'everyday', 'everyday of the year', 'everyday of the week'],
    'SOCIAL' : ['social', 'extroverted', 'socialable', 'outgoing', 'friendly'],
    'SPENDING TIME ON MY OWN' : ['spending time on my own', 'relaxing by myself', 'hanging out by myself', 'taking time to myself', 'take time away from others'],
    'SAME' : ['same', 'exact same', 'opposite', 'exact opposite', 'same as me'],
    'PYTHON' : ['Python', 'Java', 'CSS', 'C++', 'SQL'],
    'LEARN' : ['learn', 'understand', 'master', 'grasp', 'interpret'],
    'IMPROVE' : ['improve', 'get better', 'progress', 'develop', 'slowly get better'],
    'ANIMALS' : ['animals', 'clowns', 'heights', 'the dark', 'enclosed spaces'],
    'AGE' : ['8', '9', '10', '11', '12'],
    'OVERCOME' : ['overcome', 'get past', 'beat', 'defeat', 'move past'],


        } 
# FIXME:
# copy your generate_comment function from the madlibs assignment here

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 
parser = argparse.ArgumentParser(description='Add username from command line')
parser.add_argument('--name', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.username)
my_bot = 'cgaylord25bot' + args.username

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/z1k7ax/potato_subreddit/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 2
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    print('before .replace_more()')
    submission.comments.replace_more(limit=None, threshold=0)
    print('after .replace_more()')
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != 'cgaylord25bot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        print(datetime.datetime.now(), ': top level comment')
        submission.reply(generate_comment())

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []

        for comment in not_my_comments:
            has_not_replied = True
            for reply in comment.replies:
                if reply.author == 'cgaylord25bot':
                    has_not_replied = False
                    break
            if has_not_replied == True:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            randomizing_comments = random.choice(comments_without_replies)
            try:
                largest_number_of_upvotes = 0
                for new_comment in comments_without_replies:
                    if new_comment.score > largest_number_of_upvotes:
                        largest_number_of_upvotes = new_comment.score
                        largest_number_of_upvotes = new_comment
                largest_number_of_upvotes.reply(generate_comment())
            except praw.exceptions.APIException:
                print('deleted comment, no reply option')
        except IndexError:
            print('all comments are mine')

        # FIXME (task 5): select a new submission for the next iteration;
        # your newly selected submission should be randomly selected from the 5 hottest submissions
        submission = random.choice(list(reddit.subreddit('cs40_2022fall').hot(limit=5)))

        # We sleep just for 1 second at the end of the while loop.
        # This doesn't avoid rate limiting
        # (since we're not sleeping for a long period of time),
        # but it does make the program's output more readable.
        time.sleep(5)

        #can only make 1 top valid comment