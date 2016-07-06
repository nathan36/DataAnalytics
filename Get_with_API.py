from tweepy import AppAuthHandler
from tweepy import API
from tweepy import TweepError
from GetOldTweets import manager
import time

access_token = "707079396922773504-Vr0Com9qRPepTEudQhq03Lhe8zYAXwv"
access_token_secret = "ycmLrMJBehXUa05aha3ETjDyvhhHeKrVJ2DVpAK9CEkyU"
consumer_key = "DYbUqhruqZZbqiEU0smju3sRk"
consumer_secret = "JpxYvtCtHIsV3E0IuRWG9DvhejpsdqHq8SxL75fM5hDt88nFAx"

auth = AppAuthHandler(consumer_key, consumer_secret)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# set search key word, data range and maximum number of tweets for capturing
tweetCriteria = manager.TweetCriteria().setQuerySearch('TEXT')\
    .setSince("yyyy-mm-dd").setUntil("yyyy-mm-dd").setMaxTweets(100000)

data = manager.TweetManager.getTweets(tweetCriteria)

tweet = str(time.time()) + '_' + 'twitter_data.txt'

with open(tweet, 'w') as outfile:
    for line in data:
        try:
            outfile.write(line.text.encode('utf-8'))
            outfile.write("\n")
        except TweepError:
            continue
