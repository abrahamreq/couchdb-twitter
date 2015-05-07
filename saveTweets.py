# -*- coding: UTF-8 -*-

from tweetStore import TweetStore
from TwitterAPI.TwitterAPI import TwitterAPI

# Your Twitter authentication credentials...
API_KEY = 'Rellenar con tus credenciales'
API_SECRET = 'Rellenar con tus credenciales'
ACCESS_TOKEN = 'Rellenar con tus credenciales'
ACCESS_TOKEN_SECRET = 'Rellenar con tus credenciales'


storage = TweetStore('nombreBD')
api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
for item in api.request('statuses/filter', {'track':'PalabraAFiltrar'}):
    if 'text' in item:
        #print ('%s -- %s\n' % (item['user']['screen_name'],item['text']))
        print (item['user']['screen_name'], item['text'])
        storage.save_tweet(item)
    elif 'message' in item:
        print('ERROR %s: %s\n' % (item['code'], item['message']))
        




