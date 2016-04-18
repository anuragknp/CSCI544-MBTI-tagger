__author__ = 'Anirudh'

import sys

type = 'out_training'

MODEL_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\17thApril\\',type,'_final.txt'])
modelfile = open(MODEL_FILE, 'r')
onedict = {}

ONE_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','1.txt'])
file1 = open(ONE_FILE,'w')

TWO_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','2.txt'])
file2 = open(TWO_FILE,'w')

THREE_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','3.txt'])
file3 = open(THREE_FILE,'w')

FOUR_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','4.txt'])
file4 = open(FOUR_FILE,'w')

FIVE_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','5.txt'])
file5 = open(FIVE_FILE,'w')

SIX_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','6.txt'])
file6 = open(SIX_FILE,'w')

SEVEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','7.txt'])
file7 = open(SEVEN_FILE,'w')

EIGHT_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','8.txt'])
file8 = open(EIGHT_FILE,'w')

NINE_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','9.txt'])
file9 = open(NINE_FILE, 'w')

TEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','10.txt'])
file10 = open(TEN_FILE,'w')

ELEVEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','11.txt'])
file11 = open(ELEVEN_FILE,'w')

TWELVE_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','12.txt'])
file12 = open(TWELVE_FILE,'w')

THIRTEEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','13.txt'])
file13 = open(THIRTEEN_FILE,'w')

FOURTEEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','14.txt'])
file14 = open(FOURTEEN_FILE,'w')

FIFTEEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','15.txt'])
file15= open(FIFTEEN_FILE,'w')

SIXTEEN_FILE = ''.join(['D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Naive-Bayes-Files\\17thApril\\training\\','16.txt'])
file16 = open(SIXTEEN_FILE,'w')


# , , , , , , ,

for line in modelfile:

    mylist = line.split(',')

    if mylist[0] == 'labels':
        continue

    if (mylist[0]) == 'INTJ':
        file1.write(mylist[1])

    if (mylist[0]) == 'INTP':
        file2.write(mylist[1])

    if (mylist[0]) == 'ISFJ':
        file3.write(mylist[1])

    if (mylist[0]) == 'ISFP':
        file4.write(mylist[1])

    if (mylist[0]) == 'ISTJ':
        file5.write(mylist[1])

    if (mylist[0]) == 'ISTP':
        file6.write(mylist[1])

    if (mylist[0]) == 'ENFJ':
        file7.write(mylist[1])

    if (mylist[0]) == 'ENFP':
        file8.write(mylist[1])

# , , , , , , , , ''

    if (mylist[0]) == 'ENTJ':
        file9.write(mylist[1])

    if (mylist[0]) == 'ENTP':
        file10.write(mylist[1])

    if (mylist[0]) == 'ESFJ':
        file11.write(mylist[1])

    if (mylist[0]) == 'ESFP':
        file12.write(mylist[1])

    if (mylist[0]) == 'ESTJ':
        file13.write(mylist[1])

    if (mylist[0]) == 'INFJ':
        file14.write(mylist[1])

    if (mylist[0]) == 'INFP':
        file15.write(mylist[1])

    if (mylist[0]) == 'ESTP':
        file16.write(mylist[1])

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()
file11.close()
file12.close()
file13.close()
file14.close()
file15.close()
file16.close()