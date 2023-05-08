import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret

# Create API object




api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


user = api.get_user(screen_name= "sovereignchris")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")

with open("follower.txt","w",encoding="utf-8",errors="replace") as f:
    for follower in user.followers():
        f.write(follower.name)