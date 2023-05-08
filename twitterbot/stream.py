import json
import tweepy

class MyStreamListener(tweepy.StreamingClient):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
# Authenticate to Twitter
auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret


# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets_listener = MyStreamListener(api)

stream = tweepy.Stream(access_token="3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w",access_token_secret="TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p",consumer_key="vmvWDivnn4cUFkcqCj6ITOWSD",consumer_secret="HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])