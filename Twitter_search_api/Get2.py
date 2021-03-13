import twint

tweets = []
keyword = "unbounce"
start_dt = "2021-01-01"
end_dt = "2021-03-12"

c = twint.Config()
c.Since = start_dt
c.Until = end_dt
c.Search = keyword
c.Pandas = True
twint.run.Search(c)
tweets_dt = twint.storage.panda.Tweets_df

tweet = '../Data/' + 'twitter_' + keyword + '.txt'
with open(tweet, 'w') as outfile:
    for item in tweets_dt.tweet:
        try:
            outfile.write(item)
            outfile.write("\n")
        except:
            continue
