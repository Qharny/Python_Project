import tweepy

consumer_key = 'your_key'
consumer_secret = 'your_secret'
access_token = 'your_token'
access_token_secret = 'your_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('Hello, this is a test tweet from Python!')