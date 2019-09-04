# Chapter 11 Section 3 Exercise 4

import sys

def file_dict(filename= 'words.txt'):
    """ Exercise 1 """
    fin = open(filename)
    dict_ = dict()
    for word in fin:
        dict_[word.strip()] = 1
    fin.close()
    return dict_

def histogram(s): 
    """ Exercise 2 """
    d = dict() 
    for c in s: 
        d[c] = d.get(c,0) + 1
    return d

def print_hist(h):
    """ Exercise 3 """
    lis = []
    for c in h:
        lis.append([c,h[c]])
    lis.sort()
    for c in lis:
        print c, lis[c], '\n'

def reverse_lookup(d, v):
    """ Exercise 4 """
    keys = []
    for k in d:
        if d[k] == v: keys.append(k)
    return keys

if __name__ == '__main__':

    dict_ = file_dict(*sys.argv)
    hist = histogram(dict_)
    print_hist(hist)
