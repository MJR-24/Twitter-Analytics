# Imports
import tweepy
from tweepy import tweet
from tweepy.api import API

# Variables for user credentials for Twitter API
access_token = "24816620-I85JgN7tSuv1SgIXGHzivECgS5PBg4Smc2TyPxdLK"
access_token_secret = "YmeOrculf2RwJ711CwB9PlKhvG7cT8B9eCvblRuTkPQBp"
consumer_key = '5cSivldEXb2MbHhPD4vxc1tYQ'
consumer_secret = 'f7m267xOpEC2b9oQYbCW0mfhGCdcmHt9hQXYSZUAAqiSflBfUc'

# Creating API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting access token and secret
auth.set_access_token(access_token,access_token_secret)

# Creating API object while passing in auth info
api = tweepy.API(auth)

# 1. Timeline query:
""" 
publicTweets = api.home_timeline()
for tweet in publicTweets:
    print(f'Text: {tweet.text}')
    print(f'Time: {tweet.created_at}')
    print(f'User: {tweet.user.screen_name}')
    print(f'Location: {tweet.user.location}')
    print('###') """

# 2. User tweets:
""" 
name = 'SpaceX'
tweetCount = 5
results = api.user_timeline(id=name,count=tweetCount)
for tweet in results:
    print(tweet.text) """

# 3. Finding Tweets using keywords:

query = 'SpaceX'
language = 'en'
results = api.search_tweets(q=query,lang=language)
for tweet in results:
    print(tweet.user.screen_name, "Tweeted: ",tweet.text)
