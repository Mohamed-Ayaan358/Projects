from textblob import TextBlob
import tweepy
import sys

api_key='GnVEdbt7khqLvMRZVtFYjESZE'
api_key_secret='6yfEBej2M33cQmtFVYfCW1rhKguDaBccJed4vmjUQO1VLsYuZZ'
access_token='1330406436409524224-npTMJl5GzOHgd86824OWriUJoUks4c'
access_token_secret='IL0fZXZwzkVirv4b2cBwuNKejt1yZzXq7ZQ7wL1zowid0'

auth_handler= tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth_handler)

public_tweets=api.home_timeline()
for tweets in public_tweets:
	print(tweets.text)
	