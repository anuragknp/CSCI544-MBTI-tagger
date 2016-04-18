__author__ = 'Anirudh'

import csv
import codecs

type = 'out_testing'

#type = 'out_training'

list = ['INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'INFJ', 'INFP', 'ESTP']

dict_filetypes = {}


count = 1

for item in list:
    if item == 'INTJ':
        dict_filetypes['INTJ'] = count
    else:
        dict_filetypes[item] = count
    count+=1


MODEL_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_final.txt'])
filemodel = open(MODEL_FILE, 'w')

LDA_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_lda_final.txt'])
ldafile = open(LDA_FILE, 'w')

NAME_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_names.txt'])
namefile = open(NAME_FILE,'r')

TAG_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_tags.txt'])
tagfile = open(TAG_FILE,'r')

TWEET_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Filtered\\17thApril\\',type,'_tweets_filtered.txt'])
tweetfile = open(TWEET_FILE,'r')

name = namefile.readline()
lineno = tagfile.readline()
tweet = tweetfile.readline()



filemodel.write('labels'+','+'tweets'+"\n")

while lineno and tweet:

    if tweet != 'nopropertweet\n':
        lineno=lineno.strip("\n")
        filemodel.write(lineno +","+tweet)

        lineno = lineno.strip(codecs.BOM_UTF8)
        ldafile.write(str(dict_filetypes[lineno])+","+tweet)
    else:
        print 'no proper tweet'

    lineno = tagfile.readline()
    tweet = tweetfile.readline()
    name = namefile.readline()