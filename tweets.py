import snscrape.modules.twitter as sntwitter
import pandas as pd
import pytz
from Tweets import Tweets
from pydantic import BaseModel
from fastapi import FastAPI

def getTweetsByUserDate(data):

    query = '(from:{0}) since:{1} -filter:replies'.format(data.user_name,data.date)
    
    print(query)
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        utc_date = tweet.date
        brasilia_tz = pytz.timezone('America/Sao_Paulo')
        br_date = utc_date.astimezone(brasilia_tz)
        tweets.append({
            'id':tweet.id,
            'user_name':tweet.user.username,
            'content':tweet.rawContent,
            'url':tweet.url,
            'date':br_date.strftime("%Y-%m-%d %H:%M")
        })
    
    tweets = sorted(tweets, key=lambda x: x['date'], reverse=True)
    
    return tweets

def get_twitter_profile_info(data):
    # Pesquisar pelo nome de usuário do Twitter
    search_query = '(from:{0})'.format(data.user_name)
    print(search_query)
    # Executar a pesquisa usando snscrape
    for profiles in sntwitter.TwitterSearchScraper(search_query).get_items():

        if profiles:
            # Obter o primeiro tweet que corresponde ao nome de usuário
            user = profiles.user

            user_info = {
                'id': user.id,
                'user_name': user.username,
                'display_name': user.displayname,
                'profile_image_url': user.profileImageUrl,
                'profile_banner_url': user.profileBannerUrl
            }

            return user_info
        
        else: return []



# user = get_twitter_profile_info('elonmusk')
# print(user)

# tweets = getTweetsByUserDate('elonmusk','2023-05-29')
# print(tweets)

app = FastAPI()

def testPost(data):
    print('DATAA =>',data)
    return {'opa':'DALEE NESSA PORRA'}


class ProfileDate(BaseModel):
    user_name: str
    date: str

@app.post("/api/twitter/get_tweets_profile_date")
def twitterGetTweetsProfileDate(data: ProfileDate):
    response = getTweetsByUserDate(data)
    return response 

class ProfileDate(BaseModel):
    user_name: str

@app.post("/api/twitter/get_profile")
def twitterGetProfile(data: ProfileDate):
    response = get_twitter_profile_info(data)
    return response



