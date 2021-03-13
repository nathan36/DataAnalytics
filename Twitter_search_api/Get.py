from tweepy import API
from tweepy import AppAuthHandler
from tweepy import TweepError
from TweetCriteria import TweetCriteria
from TweetManager import TweetManager
import time

access_token = "707079396922773504-Vr0Com9qRPepTEudQhq03Lhe8zYAXwv"
access_token_secret = "ycmLrMJBehXUa05aha3ETjDyvhhHeKrVJ2DVpAK9CEkyU"
consumer_key = "DYbUqhruqZZbqiEU0smju3sRk"
consumer_secret = "JpxYvtCtHIsV3E0IuRWG9DvhejpsdqHq8SxL75fM5hDt88nFAx"

auth = AppAuthHandler(consumer_key, consumer_secret)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# set search key word, data range and maximum number of tweets for capturing
# Note: twitter search api unstable, for first time search, since unit period
# recommend to be less than a month

keyword = "unbounce"
tweetCriteria = TweetCriteria().setQuerySearch(keyword)\
    .setSince("2020-01-01").setUntil("2021-03-12").setMaxTweets(0)

data = TweetManager.getTweets(tweetCriteria)

tweet = '../Data/' + 'twitter_' + keyword + '.txt'
with open(tweet, 'w') as outfile:
    for line in data:
        try:
            outfile.write(line.text)
            outfile.write("\n")
        except TweepError:
            continue
