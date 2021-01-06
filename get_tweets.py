import tweepy
import re

from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def get_tweets():
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, id='EvilAFM').items():
        tweets.append(tweet.text)

    #quitar links y menciones
    text = ' '.join(tweets)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\S+", "", text)

    f = open("tweets.txt", "w", encoding='utf-8')
    f.write(text)
    f.close()

def main():
    global api
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    get_tweets()

if __name__ == '__main__':
    main()
else:
    print('NO')

