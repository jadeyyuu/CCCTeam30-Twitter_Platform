import tweepy

auth = tweepy.OAuthHandler("mHwDkHtAr0YsmrJhuVpA9MQhH", "8OXET1pwHp70H1R5Ed0w9NEeBXrZVJOqa9JLbgEtO6xjLq8OlV")
auth.set_access_token("1384514435385937926-ufOKI9oTRQrM0ibYTpRBDIuR7klIYC", "0NNpZ0zPHWylv7p6MLPwjoZPuCZsqHXsbBNS00GElwfTX")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))
