import pandas as pd
import Function as fun

# point to the text file with captured tweets
tweets_data_path = './Data/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweets_data.append(line)
    except:
        continue

# filter tweets with condition
tweets = pd.DataFrame(tweets_data)
tweets['cond'] = tweets[0].apply(lambda x: fun.word_search('changing', x)
                                            or fun.word_search('revenue', x))
tweets['text'] = tweets[tweets['cond'] == True][0]

# combine text into single string for word cloud processing
combine = " ".join(tweets_data)
text = combine.lower()
filter_text = " ".join([word for word in text.split()
                            if 'http' not in word
                            and not word.startswith('@')
                            and 'RT' not in word
                            and 'hootsuite' not in word
                            and 'twitter' not in word
                            and 'social' not in word
                            and 'media' not in word
                            and 'pic' not in word
                            and 'thank' not in word
                            ])

# create word cloud
fun.draw_wordcloud(filter_text, "./twitter_mask.png")
