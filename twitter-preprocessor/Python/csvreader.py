__author__ = 'Anirudh'

import csv

type = 'out'

MODEL_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\',type,'.txt'])
file = open(MODEL_FILE, 'r')

TAG_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\',type,'_tags.txt'])
tagfile = open(TAG_FILE,'w')


TWEET_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\',type,'_tweets.txt'])
tweetfile = open(TWEET_FILE,'w')


for line in file:
    line = line.replace('\r', '')
    mylist = line.split(',')
    if len(mylist) < 2:
        continue

    tagfile.write(str(mylist[0])+'\n')
    tweetfile.write(mylist[1])


# while row:
#
#     if(row[0] in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]):
#         tagwriter.write(int(row[0])+1)
#         tweetwriter.write(row[1])
#
#     row = csv_reader.next()
