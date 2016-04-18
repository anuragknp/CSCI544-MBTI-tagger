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

def get_tag_count(tt, tag):
    if tag not in tt:
        return 0
    return tt[tag]

for u in user.keys():
    tag = {}
    for t in user[u]:
        t = list(t.lower())
        for tt in t:
            if tt not in tag:
                tag[tt] = 1
            else:
                tag[tt] += 1
    ans = ''
    if get_tag_count(tag, 'i') < get_tag_count(tag, 'e'):
        ans += 'I'
    else:
        ans += 'E'

    if get_tag_count(tag, 'n') < get_tag_count(tag, 's'):
        ans += 'N'
    else:
        ans += 'S'

    if get_tag_count(tag, 't') < get_tag_count(tag, 'f'):
        ans += 'T'
    else:
        ans += 'F'
    
    if get_tag_count(tag, 'j') < get_tag_count(tag, 'p'):
        ans += 'J'
    else:
        ans += 'P'

    user[u] = ans

with open('unique_users_best_tag2.txt', 'w') as out:
    out.write(json.dumps(user))
