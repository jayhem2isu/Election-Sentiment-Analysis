#written in python 3
import tweepy
from tweepy import OA


#app credentials
consumer_key = 'Qd0pRJziw6VdzE2RQqU0oghFh'
consumer_secret = 'LzEzsUPbMkKpwW3fviMc8uLiUvJx9XVolcYfHZxVKjSZzjafnR'
access_token ='817527981329514496-LUdPSX4o02GDzbJZOZkMMRgn8xd3dmt'
access_token_secret = 'u3EbYVLnoQnnQ9IAA0oru4JfTJDAj7gZbABOIda0EKUpZ'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)
