import markovify
import tweepy

from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

DEBUG = True
SOURCE_TEXT = 'tweets.txt'

def generate_text():
    with open(SOURCE_TEXT) as f:
        text = f.read()
    text_model = markovify.Text(text)
    return text_model.make_sentence()

def main():
    global api
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweet_ready = generate_text()

    if DEBUG:
        print(tweet_ready)
    else:
        api.update_status(tweet_ready)
        print("Enviado: " + tweet_ready)

if __name__ == '__main__':
    main()

