# -*- coding=utf-8 -*-

__author__ = 'Anirudh'

import random
import csv
import nltk
import codecs
import json

perso_types = ['INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'INFJ', 'INFP', 'ESTP']

train_path_template = "D:\Curriculum\Natural-Language-Processing\Directed-Research\AllData\Naive-Bayes-Tokens\\17thApril\\train\\"
test_path_template = "D:\Curriculum\Natural-Language-Processing\Directed-Research\AllData\Naive-Bayes-Tokens\\17thApril\\test\\"

train_set = []
test_set = []
for i in range(1,17):
    perso_type = perso_types[i-1]
    #dit = train_file.read()
    train_file = codecs.open(train_path_template + str(i) + ".txt" ,'r',encoding='utf-8')
    train_features = json.loads(train_file.read())
    train_set.append((train_features, perso_type[1]))

    test_file = codecs.open(test_path_template + str(i) + ".txt" ,'r',encoding='utf-8')
    test_features = json.loads(test_file.read())
    #test_features = train_features

    test_set.append((test_features, perso_type[1]))

classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(10)