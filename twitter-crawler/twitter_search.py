from TwitterSearch import *
import time
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


sessions = [TwitterSearch(
         )]

current_session = 0

def search():
    for hash in ['INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'INFJ', 'INFP', 'ESTP']:
        tso = TwitterSearchOrder()
        tso.set_keywords(["#"+hash])
        tso.set_language('es')
        tso.set_include_entities(False)

        ts = sessions[current_session]

        c = 0
        with open(hash+'.'+'es', 'ab') as out:
            worked = False
            while not worked:
                try:
                    tweet_list = ts.search_tweets_iterable(tso)
                    worked = True
                except TwitterSearchException as e:
                    global current_session
                    current_session += 1
                    if current_session > 3:
                        current_session = 0
                        time.sleep(15*60)
                    ts = sessions[current_session]

            for tweet in tweet_list:
                out.write(tweet['user']['screen_name']+'|$$$$$$|'+tweet['text']+'\n')
                c += 1
                print tweet['text']

        print hash, c


if __name__=='__main__':
    search()
