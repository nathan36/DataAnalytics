import json
import pandas as pd
import numpy as np
import Function as fun

# point to the text file with captured tweets
tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        # tweets_data.append(line)
        tweet = json.load(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame(tweets_data)
tweets['cond1'] = tweets[0].apply(lambda x: fun.word_search('changing', x)
                                            or fun.word_search('revenue', x))
tweets['text'] = tweets[tweets['cond1'] == True][0]
print tweets['text']

tweets['text'] = map(lambda tweet: tweet['text'] if 'text' in tweet else np.nan, tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'] if 'lang' in tweet else np.nan, tweets_data)
tweets['country'] = [tweet['place']['country'] if "place" in tweet and tweet['place'] else np.nan for tweet in
                     tweets_data]

# filter tweets by lang and context relevance
df = pd.DataFrame.dropna(tweets)
df_tweets = df[df.lang == 'en']
df_tweets['relevant'] = df_tweets['text'].apply(lambda tweet: fc.word_search('TEXT', tweets_data))

# combine text into single string for word cloud processing
text = " ".join(df_tweets[['relevant'] == True]['text'])

text = " ".join(tweets_data)
no_urls_no_tags = " ".join([word for word in text.split()
                            if 'http' not in word
                            and not word.startswith('@')
                            and word != 'RT'
                            ])

# create word cloud
fun.draw_wordcloud(no_urls_no_tags, "./twitter_mask.png")
