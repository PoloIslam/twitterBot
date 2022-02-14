#3.7 version of tweepy, time module, and dog API
import tweepy
import time
import dog

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

            

#post a dog every hour
def HourlyDog():
    pic = api.media_upload(dog.getDog(filename='randog'))
    api.update_status(media_ids=[pic.media_id])
    print("Posting Dog...")
    time.sleep(60)

    


while True:
    HourlyDog()
