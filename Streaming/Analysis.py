import json
import pandas as pd
import numpy as np
from Function import word_search
from Function import draw_wordcloud

# point to the text file with captured tweets
tweets_data_path = '../Data/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'] if 'text' in tweet else np.nan, tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'] if 'lang' in tweet else np.nan, tweets_data)
tweets['country'] = [tweet['place']['country'] if "place" in tweet and tweet['place'] else np.nan for tweet in
                     tweets_data]

# filter tweets by lang and context relevance
tweets_en = tweets[tweets['lang'] == 'en']
tweets_en['relevant'] = tweets_en['text'].apply(lambda tweet: word_search('iphone', tweet))

# combine text into single string for word cloud processing
text = " ".join(tweets['text'])
filter_text = " ".join([word for word in text.split()
                            if 'http' not in word
                            and not word.startswith('@')
                            and 'RT' not in word
                            ])


# create word cloud
draw_wordcloud(filter_text, "../twitter_mask.png")

