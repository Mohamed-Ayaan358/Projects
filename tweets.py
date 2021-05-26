from textblob import TextBlob
import tweepy
import sys
import config

auth_handler= tweepy.OAuthHandler(consumer_key=config.api_key,consumer_secret=config.api_key_secret)
auth_handler.set_access_token(config.access_token,config.access_token_secret)

api=tweepy.API(auth_handler)

public_tweets=api.home_timeline()
for tweets in public_tweets:
	print(tweets.text)
	