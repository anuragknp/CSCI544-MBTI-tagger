import nltk
import codecs
import os
from collections import defaultdict

perso_types = ['INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'INFJ', 'INFP', 'ESTP']

train_path_dir = os.getcwd() + '/training/tri-gram/'
test_path_dir = os.getcwd() + '/testing/tri-gram/'
#train_path_dir = os.getcwd() + '/training/tri-gram/'
#test_path_dir = os.getcwd() + '/testing/tri-gram/'

train_set = []
test_set = []
for i in range(1,17):
    perso_type = perso_types[i-1]
    train_file = codecs.open(train_path_dir + perso_type + ".txt", 'r', encoding='utf-8')
    test_file = codecs.open(test_path_dir + perso_type + ".txt", 'r', encoding='utf-8')
    train_features = defaultdict()
    test_features = defaultdict()

    for line in train_file:
        tokens = line.strip().split('=')
        tweet, count = tokens[0], int(tokens[1])
        train_features[tweet] = count

    for line in test_file:
        tokens = line.strip().split('=')
        tweet, count = tokens[0], int(tokens[1])
        test_features[tweet] = count

    train_set.append((train_features, perso_type[3]))
    test_set.append((test_features, perso_type[3]))

classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(10)
