import os
import time
import sys
import json
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from rauth import OAuth1Session


sessions = [OAuth1Session(consumer_key = '',
                            consumer_secret = 'TGLdiOI',
                            access_token = '181MTLcvGhP2GYy5',
                            access_token_secret = 'MSSdDtIlL9wQsYa'),

current_session = 0


def get_tweets(handle, max_id):
    params = {'screen_name': handle,
              'include_rts': 0,
              'count': 150}
    if max_id:
        params['max_id'] = max_id
    worked = False
    session = sessions[current_session]
    while not worked:
        try:
            r = session.get('https://api.twitter.com/1.1/statuses/home_timeline.json',
                                              params=params, verify=True)
            res = r.json()
            res[0]
            worked = True
        except Exception as e:
            global current_session
            current_session += 1
            if current_session > 3:
                current_session = 0
                time.sleep(15*60)
            session = sessions[current_session]

    tweets = []
    max_id = -1
    for r in res:
        tweets.append(r['text'])
    max_id = r['id']
    return tweets, max_id

  
#clean duplicates
#ls *.csv | xargs -I{} python remove_dups.py {}
#os.system('ls *.csv | xargs -I{} python remove_dups.py {}')


done = {'users': []}
try:
  with open('state.info') as state:
    global done
    done = json.loads(state.read())
except Exception as e:
  pass

users = json.loads(open('unique_users_best_tag.txt').read())

for user in users:
    if user in done['users']:
        print user
        continue

    tag = users[user]
    out = open(tag+'.txt', 'ab')
    print "handle: ", user

    tweets, max_id = get_tweets(user, None)
    while max_id != -1:
        for t in tweets:
            print t
            out.write(t+'\n')
        tweets, max_id = get_tweets(user, max_id)

    done['user'].append(user)
    with open('state.info', 'w') as state:
        state.write(json.dumps(done))
