import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import date
import json
import pprint
import certifi
import streamlit as st

#Connecting to the database
username=st.secrets['Mongo_username']
password=st.secrets['Mongo_pwd']
@st.cache_resource
def connect_db(username,password):
    try:
      con=MongoClient("mongodb+srv://"+username+":"+password+"@cluster0.2lvjncx.mongodb.net/?retryWrites=true&w=majority",
                      tlsCAFile=certifi.where())
      return con
    except ConnectionFailure:
        return 'Fail'
    except:
        return 'Fail'
    
@st.cache_data
def convert_to_df(input_data):
   tweets_df2 = pd.DataFrame(input_data,
                             columns=['Date', 'Tweet Id','URL','UserName', 'Content', 'ReplyCount',
                            'RetweetCount','Language','Source','LikeCount'])
   
   return tweets_df2
  
#Scrapping the data from twiiter
def scrap(final_query,limit):
    limit=int(limit)
    tweets_list2 = []
   
#Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(final_query).get_items()):
        if i==limit:
            break
        tweets_list2.append([ tweet.date, tweet.id,tweet.url,tweet.user.username,
                              tweet.content,tweet.replyCount,tweet.retweetCount,
                              tweet.lang,tweet.source,tweet.likeCount])

    tweets_df2 = convert_to_df(tweets_list2)
    #tweets_df2.to_json('file.json', orient = 'records', compression = 'infer', index = 'true')
    return tweets_list2

def insert_data(query_text,tweets_list2):
    if len(tweets_list2) !=0 : 
        
        client = connect_db(username,password)
        if client!='Fail':
            db = client.twitterscrap
            document=db.scrap_data
            tweets_df2 = convert_to_df(tweets_list2)
            result = tweets_df2.to_json(orient="records")
            parsed = json.loads(result)
            pprint.pprint(parsed)
            currentdate=str(date.today())
            mystore= {'Scraped Word': query_text,
                      'Scraped Date':currentdate,
                      'Scraped Data' :parsed}
            x = document.insert_one(mystore)
            print(x.inserted_id)
            return 'Successfully uploaded'
        else:
            return 'Sorry,Not able to connect to Database.'
    else :
        return 'No tweets are found'

