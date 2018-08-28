# -*- coding: utf-8 -*-
# open lines_read.csv file and count number-of-lines
# open lines_alphabetised file and get number-of-lines + 1
# tweet the line, append to lines_read file with time and link to tweet

import tweepy
import os
from datetime import datetime

# this authentication method is described [here](https://slackapi.github.io/python-slackclient/auth.html)
# basically, when the command is run, instead of running:
# $ python bot.py
# we run:
# $ consumer_key="YOUR_KEY_HERE" consumer_secret="YOUR_SECRET_HERE" access_token="YOUR_ACCESS_TOKEN_HERE" access_token_secret="YOUR_ACCESS_TOKEN_SECRET_HERE" python bot.py
# this passes these variables into the python script
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]

# print (auth_token, auth_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# how many lines have we written already?
num_lines = sum(1 for line in open('lines_read.csv'))
print(num_lines)

# function for splitting long lines (some are very long)
# splits strings into manageble chunks by word
def split_string(str, limit, sep=" "):
    words = str.split()
    if max(map(len, words)) > limit:
        raise ValueError("limit is too small")
    res, part, others = [], words[0], words[1:]
    for word in others:
        if len(sep)+len(word) > limit-len(part):
            res.append(part)
            part = word
        else:
            part += sep+word
    if part:
        res.append(part)
    return res


f = open('movie_lines-alphabetised.txt')
for i, line in enumerate(f):
	if i == num_lines:
		print(line, len(line))
		with open('lines_read.csv','a') as g:
			tweets = split_string(str=line, limit=250)
			if (len(tweets) == 1):
				print(tweets[0])
				try:
					api.update_status(tweets[0])
				except tweepy.error.TweepError:
				    pass
			else:
				for counter, value in enumerate(tweets):
					if (counter == 0):
						content = value+"…"
						try:
							api.update_status(content)
						except tweepy.error.TweepError:
							pass 
					elif (counter == len(tweets)-1):
						content = "…"+value
						try:
							api.update_status(content)
						except tweepy.error.TweepError:
							pass 
					else:
						content = value+"…"
						try:
							api.update_status(content)
						except tweepy.error.TweepError:
							pass 
			# api.update_status(line)
			update = str(datetime.now()) + "," + str(len(tweets)) + "," + str(line)
			g.write(update)
