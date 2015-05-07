# -*- coding: utf-8 -*

import couchdb,tweetStore
from django.utils.regex_helper import contains
from _codecs import encode
from operator import itemgetter
from tweetStore import TweetStore
# server = couchdb.Server()
# 
# 
# storage = tweetStore.TweetStore('pp')
# palabra = ["arandela","pacto","ganar"]
# comprueba = lambda p,t: p in t
# for tweet in storage.get_tweets():
#     for p in palabra:
#         if(comprueba(p,tweet.value['text'])):
#            print tweet.value['text'], tweet.value['_rev'], tweet.value['user']['screen_name']
#            print tweet.value['retweeted_status']['retweet_count'], tweet.value['user']['favourites_count'], tweet.value['text'] , '\n'
#             
# print storage.count_tweets()

def ordena_palabras(bd):
    server = couchdb.Server()
    storage = tweetStore.TweetStore(bd)
    dic = {}
    print storage.count_tweets()
    for tweet in storage.get_tweets():
        textoCompleto = tweet.value['text']
        palabras = textoCompleto.split(' ')
        for p in palabras:
            if(len(p)>3):
                if(dic.has_key(p)):
                    dic[p] = dic[p]+1
                else:
                    dic[p] = 1
    #print dic
    #print sorted(dic.values())
    a = sorted(dic.items(), key=itemgetter(1))
    
    print a
    print "He acabado con " + bd + " \n"
    print type(a)
    return vuelta(a)

def tweets_rt(bd):
    storage = tweetStore.TweetStore(bd)
    dic = {}
    print storage.count_tweets()
    for tweet in storage.get_tweets():
        if(tweet.value['retweeted_status']['retweet_count']>10):
            textoCompleto = tweet.value['text']
        palabras = textoCompleto.split(' ')
        for p in palabras:
            if(len(p)>3):
                if(dic.has_key(p)):
                    dic[p] = dic[p]+1
                else:
                    dic[p] = 1
    #print dic
    #print sorted(dic.values())
    a = sorted(dic.items(), key=itemgetter(1))
    
    print a
    print "He acabado con " + bd + " \n"
    print type(a)
    return vuelta(a)
            
    
def vuelta(lista):
    defi = []
    for i in range(len(lista)-1):
        defi.append(lista.pop())
    print defi
    
def contiene_todos(listaBD):
    listaBD = ['psoebd','ppbd','podemos']
    partidos = ['PSOE','PP','PODEMOS']
    tw = []
    for bd in listaBD:
        storage = tweetStore.TweetStore
        tweets = storage.get_tweets()
        for tweet in tweets:
            if(all (p in tweet.value['text'] for p in partidos)):
                tw.append(tweet.value['text'])
                

        
                
                
    

 
ordena_palabras('podemosdb')
#ordena_palabras('psoe')
#tweets_rt('prue')
#tweets_rt('ejemplo')


