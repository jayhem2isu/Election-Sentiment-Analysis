#written in python 3
import tweepy
from tweepy import OA


#app credentials
consumer_key = 'JDEPUSZZ24przoFKswEpcOSqp'
consumer_secret = 'wrysEEWxSCBG6qO9peWdsKs1RbOQ4fuwYk7y0uVMnQZDv5m2K4'
access_token ='514477387-ekoCiUdY0ol034psgq8CImzaUgUmDoEsEAYsp7Oy'
access_token_secret = 'u9wiLT94Qbu4PxgTqjXBFpKFp7V9yDF6OwLKIAfGezGJT'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)
