import tweepy
from textblob import TextBlob

consumer_key = "YzRT2uJnrY74LLjwgtfyg4Qym"
consumer_secret = "1ZqSGFkMCybPsbgf0Tkqg0Td4cMms7u9Y51SBxnSconL0oT8bX"

access_token = "749638893293621249-1vnVK5boYIc3sv2o4DYBovK4Xncf1u1"
access_token_secret = "XrDrwIsGzP5WtHfPxJzW2xG31ptnHGpGxtLocSwof70pp"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('AMLO')

for tweet in public_tweets:
	print(tweet.text)
	translatio = TextBlob(tweet.text)
	analysis = TextBlob(str(translatio.translate(to='en')))
	print(analysis.sentiment.polarity)

