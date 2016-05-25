from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "707079396922773504-Vr0Com9qRPepTEudQhq03Lhe8zYAXwv"
access_token_secret = "ycmLrMJBehXUa05aha3ETjDyvhhHeKrVJ2DVpAK9CEkyU"
consumer_key = "DYbUqhruqZZbqiEU0smju3sRk"
consumer_secret = "JpxYvtCtHIsV3E0IuRWG9DvhejpsdqHq8SxL75fM5hDt88nFAx"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status

if __name__ == '__main__':

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, StdOutListener())
    stream.filter(track=['Apple'])
