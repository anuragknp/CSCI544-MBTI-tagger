__author__ = 'Anirudh'

import csv

type = 'out_testing'

MODEL_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'.txt'])
file = open(MODEL_FILE, 'r')

NAME_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_names.txt'])
namefile = open(NAME_FILE,'w')

TAG_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_tags.txt'])
tagfile = open(TAG_FILE,'w')

TWEET_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_tweets.txt'])
tweetfile = open(TWEET_FILE,'w')


for line in file:
    line = line.replace('\r', '')
    mylist = line.split(',')
    if len(mylist) < 2:
        continue

    namefile.write(str(mylist[1])+'\n')
    tagfile.write(str(mylist[0])+'\n')
    tweetfile.write(mylist[2])
