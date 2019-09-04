from sys import *
setrecursionlimit(10000)

def useall(word, letters):
    """ Makes sure that each required letter corresponds to atleast one other letter
            within the word, in other words that all 'required' letters are used """
    truth=True
    for i in letters:
        truth=i in word and truth
    return truth

def wordlist4():
    t=[]
    fin=open ("words.txt")
    for word in fin:
        t.append(word.strip())
    return t[:]

from bisect import bisect_left

def bisect2(wordlist, word):
    " I commandeered Authors Idea of Using bisect_left built-in function "
    bis=bisect_left(wordlist, word)
    if (bis<len(wordlist)) and (wordlist[bis]==word): return bis
    else: return None

fin=open('interlock', 'w')

def interlock(wl=wordlist4(),w2=wordlist4(),w33=wordlist4()):
    """ Misunderstood prompt """
    for word1 in wl:
        for word2 in w2:
            w3=word1+word2
            for mword in w33:
                if (useall(mword, w3)) and (useall(w3, mword)) and (len(w3)==len(mword)):
                    print word1+' '+word2+' '+mword+'\r\n'

interlock()
