import tweepy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret

# Create API object


# Create a tweet

api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


"""
This will like the most recent tweet in your feed or unlike it, if liked
"""
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)