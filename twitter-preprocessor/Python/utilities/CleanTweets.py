# -*- coding: utf-8 -*-
import string
import codecs
import emoticons

exclude = set(string.punctuation)
import os

filelist = ["ENFJ", "ENFP", "ENTJ", "ENTP", "ESFJ", "INTJ", "INTP", "ISFJ", "ISFP", "ISTJ", "ISTP"]

for filename in filelist:

    readfile= ''.join(['D:\Curriculum\Natural-Language-Processing\Directed-Research\\resamplecorpus2\\',filename,'.txt'])
    source = codecs.open(readfile,"r","utf-8")

    writefile="D:\Curriculum\Natural-Language-Processing\Directed-Research\\resamplecorpus2\tokenized\ISTPcleaned.txt"
    destination = codecs.open(writefile,"w","utf-8")

    main_text = source.readline()

    while main_text:
        main_text = ''.join(ch for ch in main_text if ch not in exclude)
        n = filter(lambda x: x==' ' or x not in string.printable, main_text)
        destination.writelines(n)
        main_text = source.readline()
