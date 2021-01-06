import markovify
import tweepy

import re

from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

DEBUG = True

def generate_text(tweets):
    text = get_tweets()
    text_model = markovify.Text(text)

    return text_model.make_sentence()

def get_tweets():
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, id='EvilAFM').items():
        tweets.append(tweet.text)

    #quitar links y menciones
    text = ' '.join(tweets)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\S+", "", text)

    return text

def main():
    global api
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets = get_tweets()
    tweet_ready = generate_text(tweets)

    if DEBUG:
        print(tweet_ready)
    else:
        api.update_status(tweet_ready)
        print("Enviado: " + tweet_ready)

if __name__ == '__main__':
    main()

