import os
import time
import sys
import json
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from rauth import OAuth1Session


sessions = [OAuth1Session(consumer_key = 'mCmnUfuFDjfCQOY1s3Dg',
                            consumer_secret = '7DjY0qEupH2ROjtBCCbGXVvGwIhh7D17PnhJTGLdiOI',
                            access_token = '181620948-jaowlBpUCRPcmGPWHaWO3ZuUtrnMTLcvGhP2GYy5',
                            access_token_secret = 'MSeEXRjoQsgZtZRSdDtIlL9wQsYagjJmxCjOfuI3FroRb'),
            OAuth1Session(consumer_key = 'ZHToWTJADerVaLhuERexQGiVa',
                            consumer_secret = 'A7VpihvlyWlbBPKSyZs05BHPMDfLTjlgHKscLhyWjHmszCJAkE',
                            access_token = '236456241-3tugICvAeEF08DZ89D71L57UqwrlZaVbqC0UTzxd',
                            access_token_secret = '2fkCSiT9EVa6I73dc7SukjhzzBW1FGD9JvMXMk5SU0qRI'),
            OAuth1Session(consumer_key = 'rn6SoXfPZg7rUTtCldreOF0U6',
                            consumer_secret = 'p42IAyjAUt65y6saBeRuCvtvmpPFqKl91StZ7DDGPGE1HV1Jds',
                            access_token = '720056314928312320-AyT7SUJ6nPnomMwm62roY5WQqcteRta',
                            access_token_secret = 'CKLoyQDElEmHRmDkfyGnl07kSN6euHlZVaQoMjX910Rc0'),
            OAuth1Session(consumer_key = 'sRb0mjlzbGh0m75GXyURiUgTQ',
                            consumer_secret = 'O3973O3LYnCnKNwCDLFCho8cxYTyzXVx6mFtahkeehQTL8T2Q6',
                            access_token = '712791572551630848-nEcwYI8vwVghN5OxDJKiRARVwR4dJna',
                            access_token_secret = 'PjDlT5WCicvMi8zDBNqjR4G2LV1PfapvcnEflpFNAyThB')]

current_session = 0


def get_tweets(handle, max_id):
    params = {'screen_name': handle,
              'include_rts': 'false',
              'count': 150}
    if max_id:
        params['max_id'] = max_id
    worked = False
    session = sessions[current_session]
    while not worked:
        r = session.get('https://api.twitter.com/1.1/statuses/home_timeline.json',
                                              params=params, verify=True)
        res = r.json()
	if 'errors' in res:
	    global current_session
            current_session += 1
            if current_session > 3:
                 current_session = 0
                 print "Going to sleep ", time.time()
                 time.sleep(10*60)
            session = sessions[current_session]
	else:
            worked = True

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
    out = open('out.txt', 'ab')
    print "handle: ", user

    tweets, max_id = get_tweets(user, None)
    while max_id != -1:
        for t in tweets:
            out.write(tag+'#!#!#!'+user+'#!#!#!'+t+'\n')
        tweets, max_id = get_tweets(user, max_id)

    done['users'].append(user)
    with open('state.info', 'w') as state:
        state.write(json.dumps(done))
