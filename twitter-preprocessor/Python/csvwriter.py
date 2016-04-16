__author__ = 'Anirudh'

import csv

type = 'out'

MODEL_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\',type,'_final.txt'])
file = open(MODEL_FILE, 'w')

TAG_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\',type,'_tags.txt'])
tagfile = open(TAG_FILE,'r')

TWEET_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Filtered\\out_tweetsfiltered.txt'])
tweetfile = open(TWEET_FILE,'r')

lineno = tagfile.readline()
tweet = tweetfile.readline()

file.write('labels'+','+'tweets'+"\n")

while lineno and tweet:

    if tweet != 'nopropertweet\n':
        lineno=lineno.strip("\n")
        file.write(str(int(lineno)+1) +","+tweet)
    else:
        print 'no proper tweet'

    lineno = tagfile.readline()
    tweet = tweetfile.readline()


