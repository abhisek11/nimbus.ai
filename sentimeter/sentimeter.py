
from secrets import Oauth_Secrets
import tweepy
from textblob import TextBlob
import pandas as pd


def primary(input_hashtag):
    secrets = Oauth_Secrets()       #secrets imported from secrets.py
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    N = 1000                          #Number of Tweets
    Tweets = tweepy.Cursor(api.search, q=input_hashtag).items(N)
    # Tweets=tweepy.Cursor(api.search,q=input_hashtag + " -filter:retweets",rpp=5,lang="en", tweet_mode='extended').items(50)
    # tweets_list = []
    # for tweet in Tweets:
    #     temp = {}
    #     temp["text"] = tweet.full_text
    #     temp["username"] = tweet.user.screen_name
    #     tweets_list.append(temp)
    # print("tweets::::::",tweets_list)
    neg = 0.0
    pos = 0.0
    pos_list=[]
    nev_list=[]
    neut_list=[]
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    # data = pd.DataFrame(data=[[tweet.text,tweet.created_at,tweet.user.screen_name,tweet.user.location,tweet.user.id,tweet.user.created_at,tweet.user.description] for tweet in Tweets],
    #                 columns=['Tweets','date','user','location','id','join_date','profile_description'])
    for tweet in Tweets:
        tweet_data_dict={}
        tweet_data_dict={
                'text':tweet.text,
                'created_at':tweet.created_at,
                'screen_name':tweet.user.screen_name,
                'user_location':tweet.user.location,
                'user_id':tweet.user.id,
                'user_created_at':tweet.user.created_at,
                'tweet_user_description':tweet.user.description
            }
        
        # print(tweet.)
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:         #Negative
            neg += blob.sentiment.polarity
            neg_count += 1
            nev_list.append(tweet_data_dict)
            
        elif blob.sentiment.polarity == 0:      #Neutral
            neutral_count += 1
            neut_list.append(tweet_data_dict)
        else:                                   #Positive
            pos += blob.sentiment.polarity
            pos_count += 1
            pos_list.append(tweet_data_dict)
    # print "Total tweets",
    # print "Positive ",float(pos_count/N)*100,"%"
    # print "Negative ",float(neg_count/N)*100,"%"
    # print "Neutral ",float(neutral_count/N)*100,"%"
    print('pos_list',len(pos_list),'nev_list',len(nev_list),'neut_list',len(neut_list))
    # print(nev_list)
    return [['Sentiment', 'no. of tweets'],['Positive',pos_count]
            ,['Neutral',neutral_count],['Negative',neg_count],{'Positive_list':pos_list},
            {'Negative_list':nev_list},{'Neutral_list':neut_list}]