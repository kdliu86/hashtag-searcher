from twython import Twython
from pprint import pprint

APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

def hashtag():
    twitter = Twython(APP_KEY, APP_SECRET,
                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    # search_term = raw_input("What hashtag would you like to search for? ")
    search_term = "#thatswhatshesaid"
    d = twitter.search(q=search_term, count=100)
    counter = 0

    for tweet in d['statuses']:
        counter += 1
        try:
            pprint(str(tweet['text']))
        except:
            pprint(tweet['text'])
    print 'There are at least %i tweets for hashtag %s' % (counter, search_term)

hashtag()
