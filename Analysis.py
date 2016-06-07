import json
import pandas as pd
import numpy as np
import Function as fc

tweets_data_path = './twitter_data.txt'

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

# Filter tweets by lang and context relevance
df = pd.DataFrame.dropna(tweets)
df_tweets = df[df.lang == 'en']
df_tweets['relevant'] = df_tweets['text'].apply(lambda tweet: fc.word_search('service', tweets_data))

# Combine text into single string
text = " ".join(df_tweets[['relevant'] == True]['text'])
no_urls_no_tags = " ".join([word for word in text.split()
                            if 'http' not in word
                            and not word.startswith('@')
                            and word != 'RT'
                            ])

# fc.plot_tweets_per_category(tweets['country'], "Top 5 languages", "Language", "Number of Tweets")
# fc.plot_distribution(tweets['country'].value_counts(), "Top 5 languages", "Language", "Number of Tweets")
fc.draw_wordcloud(no_urls_no_tags, "./twitter_mask.png")
