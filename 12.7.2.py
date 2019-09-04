fin=open('words.txt')

wordlist=[]
index=0
for line in fin:
    if index==30: break
    wordlist.append(line.strip())
    index+=1
    

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

import random

def unstable_sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word)+random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


print wordlist,'\n'
print sort_by_length(wordlist),'\n'
print unstable_sort_by_length(wordlist)

