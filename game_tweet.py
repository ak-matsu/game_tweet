#https://fuyutsuki.net/python-twitter-auto/

import tweepy
import time
import schedule
import open_mv

if __name__ == '__main__':
    # 取得したアクセスキーたちをセット。
    api_key='***************'
    api_key_secret='***************'
    access_token='***************'
    access_token_secret='***************'

    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)

    number = input('1:st_message,2:end_message,3:none: ')
    number = int(number)

    if number == 1:
        api = tweepy.API(auth)
        message = message = "game_start"
        api.update_status(message)
    elif number == 2:
        api = tweepy.API(auth)
        message = "game_end"
        api.update_status(message)
        open_mv.twitch_op()
        exit
    else:
        print("none")
    exit