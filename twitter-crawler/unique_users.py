__author__ = 'anurag'
from os import listdir
from os.path import isfile, join
import json


data_folder = '/home/anurag/Documents/code/csci544/project/data'

langs = ['english', 'arabic']

user = {}

for lang in langs:
    path = data_folder + '/' + lang + '_tweets'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        for line in open(path + '/' + file, 'rb'):
            hash = file.split('.')[0]
            line = line.decode('utf-8')
            handle = line.split('|$$$$$$|')[0]
            if handle not in user:
                user[handle] = [hash]
            else:
                user[handle].append(hash)

print len(user)

with open('unique_users.txt', 'w') as out:
    out.write(json.dumps(user))

for u in user.keys():
    tag = {}
    for t in user[u]:
        if t not in tag:
            tag[t] = 1
        else:
            tag[t] += 1
    best_tag = max(tag, key=lambda i:  tag[i])
    user[u] = best_tag

with open('unique_users_best_tag.txt', 'w') as out:
    out.write(json.dumps(user))