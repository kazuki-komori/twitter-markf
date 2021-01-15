import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

def initial():
    Consumer_key = CONSUMER_KEY
    Consumer_secret = CONSUMER_SECRET
    Access_token = ACCESS_TOKEN
    Access_secret = ACCESS_SECRET

    # OAuth認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)
    API = tweepy.API(auth)
    return API