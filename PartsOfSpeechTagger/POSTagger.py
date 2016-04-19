__author__ = 'Anirudh'

import codecs
import nltk
import pyarabic

from nltk.tag import StanfordPOSTagger
nltk.internals.config_java("C:\Program Files\Java\jdk1.8.0_60\\bin\java.exe")

import os
java_path = "C:\Program Files\Java\jdk1.8.0_60\\bin\java.exe"
os.environ['JAVAHOME'] = java_path


# st = StanfordPOSTagger('english-bidirectional-distsim.tagger')

st = StanfordPOSTagger('D:\Curriculum\Natural-Language-Processing\stanford-postagger-full-2015-12-09\stanford-postagger-full-2015-12-09\models\\arabic.tagger','D:\Curriculum\Natural-Language-Processing\stanford-postagger-full-2015-12-09\stanford-postagger-full-2015-12-09\stanford-postagger.jar')
#st = StanfordPOSTagger('D:\Curriculum\Natural-Language-Processing\stanford-postagger-full-2015-12-09\stanford-postagger-full-2015-12-09\models\\english-bidirectional-distsim.tagger','D:\Curriculum\Natural-Language-Processing\stanford-postagger-full-2015-12-09\stanford-postagger-full-2015-12-09\stanford-postagger.jar')

file="arabic_in.txt"
source = codecs.open(file,"r","utf-16-be")
destination = codecs.open("utf8encoder_out.txt","wb","utf-8")
contents=source.read()
destination.write(contents)

destination = codecs.open("utf8encoder_out.txt","r","utf-8")
contents2=destination.read()

list = nltk.tokenize.wordpunct_tokenize(contents2)

for l in list:
    print l

# print contents2.split()
#
# print st.tag(contents2.split())

