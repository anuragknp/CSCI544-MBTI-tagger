__author__ = 'Anirudh'

import csv
import codecs

type = 'out_testing'

#type = 'out_training'

list = ['INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'INFJ', 'INFP', 'ESTP']

LDA_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_lda_final.txt'])
ldafile = open(LDA_FILE, 'r')


INTRO_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_lda_tf.txt'])
introfile = open(INTRO_FILE, 'w')

EXTRO_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_lda_extro.txt'])
extrofile = open(EXTRO_FILE, 'w')


for line in ldafile:

    mylist = line.split(',')
    if mylist[0] == '3' or mylist[0] == '4' or mylist[0] == '5' or mylist[0] == '6' or mylist[0] == '1' or mylist[0] == '12' or mylist[0] == '13' or mylist[0] == '16':
        introfile.write('1'+','+mylist[1])
    else:
        introfile.write('2'+','+mylist[1])
