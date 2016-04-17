import nltk
import os
import codecs

inputdirpath = os.getcwd() + '/n-gram-input-files'
trigramoutput_dirpath = os.getcwd() + '/tri-gram-output-files'
bigramoutput_dirpath = os.getcwd() + '/bi-gram-output-files'


for path, dirs, files in os.walk(inputdirpath):
    for file in files:
        inputfile = open(os.path.join(path, file), 'r')
        bigramoutputfile = open(bigramoutput_dirpath + '/' + file, 'w')
        for line in inputfile:
            for item in nltk.bigrams(line.split()):
                bigramoutputfile.write(' '.join(item))
                bigramoutputfile.write('\n')
        inputfile.close()
        bigramoutputfile.close()

for path, dirs, files in os.walk(inputdirpath):
    for file in files:
        inputfile = open(os.path.join(path, file), 'r')
        trigramoutputfile = open(trigramoutput_dirpath + '/' + file, 'w')
        for line in inputfile:
            for item in nltk.trigrams(line.split()):
                trigramoutputfile.write(' '.join(item))
                trigramoutputfile.write('\n')
        inputfile.close()
        trigramoutputfile.close()











