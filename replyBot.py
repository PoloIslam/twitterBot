#3.7 version of tweepy, time module, and dog API
import tweepy
import time
import dog

#Put your keys here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    
    print('replying to tweets...')
    #Must contain the first tweet ID to begin (1490819998637600772)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    #holds mentions
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    #prints the mention ID and its corresponding text for each mention

    for mention in reversed(mentions):
        #saves the last seen mention id and stores it into the file.
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        print(str(mention.id) + ' - ' + mention.full_text)
        replyDog(mention)
    
        
#replies to #dog with a dog pic
def replyDog(mention):
    pic = api.media_upload(dog.getDog(filename='randog'))
    if '#dog' in mention.full_text.lower():
            print('found #dog')
            print('Responding with pic...')
            api.update_status('@' + mention.user.screen_name + " Heres a dog for you!", mention.id, media_ids=[pic.media_id])
            


while True:
    reply_to_tweets()
    time.sleep(25)

