from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import TweepError
import json
import time


access_token = "707079396922773504-Vr0Com9qRPepTEudQhq03Lhe8zYAXwv"
access_token_secret = "ycmLrMJBehXUa05aha3ETjDyvhhHeKrVJ2DVpAK9CEkyU"
consumer_key = "DYbUqhruqZZbqiEU0smju3sRk"
consumer_secret = "JpxYvtCtHIsV3E0IuRWG9DvhejpsdqHq8SxL75fM5hDt88nFAx"
max_tweets = 8000

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth, wait_on_rate_limit=True)

data = Cursor(api.search, q='Hootsuite').items(max_tweets)

tweet = './twitter_data.txt'

with open(tweet, 'w') as outfile:
    for line in data:
        try:
            outfile.write(json.dumps(line._json))
            outfile.write("\n")
        except TweepError:
            time.sleep(180)
            continue