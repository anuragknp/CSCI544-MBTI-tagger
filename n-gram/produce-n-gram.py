import nltk
import os
import codecs

inputdirpath = os.getcwd() + '/n-gram-input-files'
trigramoutput_dirpath = os.getcwd() + '/tri-gram-output-files'
bigramoutput_dirpath = os.getcwd() + '/bi-gram-output-files'

def generatengram(sentence, n):
    words = sentence.split()
    if (n == 1):
        return words
    ngramlist = []
    for i in range(len(words) - 1):
        word = []
        for j in range(n):
            if ((i + j) < len(words)):
                word.append(words[i + j])
        if (len(word) == n):
            ngramlist.append(' '.join(word))
    return ngramlist

for path, dirs, files in os.walk(inputdirpath):
    for file in files:
        inputfile = open(os.path.join(path, file), 'r')
        bigramoutputfile = open(bigramoutput_dirpath + '/' + file, 'w')
        for line in inputfile:
            for item in generatengram(line, 2):
                bigramoutputfile.write(' '.join(item))
                bigramoutputfile.write('\n')
        inputfile.close()
        bigramoutputfile.close()

for path, dirs, files in os.walk(inputdirpath):
    for file in files:
        inputfile = open(os.path.join(path, file), 'r')
        trigramoutputfile = open(trigramoutput_dirpath + '/' + file, 'w')
        for line in inputfile:
            for item in generatengram(line, 3):
                trigramoutputfile.write(' '.join(item))
                trigramoutputfile.write('\n')
        inputfile.close()
        trigramoutputfile.close()
