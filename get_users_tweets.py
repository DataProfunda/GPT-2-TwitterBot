from auth_tw import get_key
import tweepy
import pandas as pd
import os 

'''
This file contains code that downloads X(Twitter) posts from particular accounts.
'''

def api():
    '''api() - function
        -------
            Returns tweepyAPI object after authentization.

    '''
    auth = tweepy.OAuthHandler(get_key("api_key"), get_key("api_key_secret"))
    auth.set_access_token(get_key("access_token"), get_key("access_token_secret"))
        
    return tweepy.API(auth)
        
#Authenticate Twitter API acces
api = api()

#List of twitter accounts used for downloading Tweets eg. 'elonmusk'
twitter_accounts = ['elonmusk']

data = []
data_user = []

df_engagment_info = pd.DataFrame(columns=['tweet','likes'])

# Loop through each Twitter account to download tweets
for user in twitter_accounts:

    
    #Limit of posts per account
    limit = 300
    
    #Create dataframe that contains account name and tweets
    columns = ['User', 'Tweets']
    
    
    stopwords = ['RT :']
    
    #Downloading extended tweets
    tweets_extended = tweepy.Cursor(api.user_timeline,
                                    screen_name = user, 
                                    count=200, tweet_mode='extended',  
                                    exclude_replies=True,
                                    include_rts=False).items(limit)
    
    
    for tweet in tweets_extended:

        likes_count = tweet.favorite_count
        retweets_count = tweet.retweet_count
        
        df_engagment_info.append([tweet.full_text,likes_count])
        
        #Checking if tweets doesn't have URL doesn't have any 
        if not any(url['url'] in tweet.full_text for url in tweet.entities['urls']):
            
            #Checking if there is not video and/or pictures
            if 'media' not in tweet.entities:
                # this tweet does not contain photos
                if not tweet.full_text.startswith('RT'):
                    data.append([tweet.full_text])
                    data_user.append([tweet.full_text])
                    
    #Save each tweets from particular account to csv file
    pd.DataFrame(data_user).to_csv(f'TWEETS/{user}_tweets.csv', sep=';', index=False)
    data_user = []

              
#Concatenating all tweets from all accounts into one file
tweets_df = pd.DataFrame()

file_list = os.listdir('TWEETS')

for user_tweets in file_list:
    user_file = pd.read_csv('TWEETS/' + user_tweets, sep=';').drop('Unnamed: 0',axis=1)
    tweets_df = pd.concat([tweets_df,user_file])

tweets_df.reset_index(drop=True).to_csv('data_tweets_full.csv', sep=';')

