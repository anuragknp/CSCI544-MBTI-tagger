# -*- coding=utf-8 -*-

import re

dict_emoji = {}

mycompile = lambda pat:  re.compile(pat,  re.UNICODE)

NormalEyes = r'[:=]'
Wink = r'[;]'

NoseArea = r'(|o|O|-)'
HappyMouths = r'[D\)\]]'
SadMouths = r'[\(\[]'
Tongue = r'[pP]'
OtherMouths = r'[doO/\\]'

Happy_RE =  mycompile( '(\^_\^|' + NormalEyes + NoseArea + HappyMouths + ')')
Sad_RE = mycompile(NormalEyes + NoseArea + SadMouths)

Wink_RE = mycompile(Wink + NoseArea + HappyMouths)
Tongue_RE = mycompile(NormalEyes + NoseArea + Tongue)
Other_RE = mycompile( '('+NormalEyes+'|'+Wink+')'  + NoseArea + OtherMouths )

Emoticon = (
    "("+NormalEyes+"|"+Wink+")" +
    NoseArea +
    "("+Tongue+"|"+OtherMouths+"|"+SadMouths+"|"+HappyMouths+")"
)
Emoticon_RE = mycompile(Emoticon)


def analyze_tweet(text):


    h= Happy_RE.search(text)
    if h:
        if 'HAPPY' in dict_emoji:
            dict_emoji['HAPPY']+=len(Happy_RE.findall(text))
        else:
            dict_emoji['HAPPY']=len(Happy_RE.findall(text))

    s= Sad_RE.search(text)
    if s:
        if 'SAD' in dict_emoji:
            dict_emoji['SAD']+=len(Sad_RE.findall(text))
        else:
            dict_emoji['SAD']=len(Sad_RE.findall(text))

    w= Wink_RE.search(text)
    if w:
        if 'WINK' in dict_emoji:
            dict_emoji['WINK']+=len(Wink_RE.findall(text))
        else:
            dict_emoji['WINK']=len(Wink_RE.findall(text))

    t= Tongue_RE.search(text)
    if t:
        if 'TONGUE' in dict_emoji:
            dict_emoji['TONGUE']+=len(Tongue_RE.findall(text))
        else:
            dict_emoji['TONGUE']=len(Tongue_RE.findall(text))


    a= Other_RE.search(text)
    if a:
        if 'OTHER' in dict_emoji:

            dict_emoji['OTHER']+=len(Other_RE.findall(text))
        else:
            dict_emoji['OTHER']=len(Other_RE.findall(text))

    return dict_emoji

if __name__=='__main__':

    #allfiles = ["INTJ","INFJ","ISTJ","ISFJ","INTP","INFP","ISTP","ISFP","ENTJ","ENFJ","ESTJ","ESFJ","ENTP","ENFP","ESTP","ESFP"]

    allfiles = ["INFJ"]

    for filename in allfiles:
        filepath = ''.join(['D:\Curriculum\Natural-Language-Processing\Directed-Research\\AllData\\Extracted\\',filename,'.txt'])

        file = open(filepath,"r")

        outputfile = open(''.join(["D:\Curriculum\Natural-Language-Processing\Directed-Research\\AllData\\Emoticons\\",filename,'_emoji.txt']),"w")

        for line in file:
            analyze_tweet(line.strip())

        for key in dict_emoji:
            outputfile.write(key+" "+str(dict_emoji[key])+'\n')

        print dict_emoji
