# Chapter 11 Section 1 Exercise 2

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

if __name__ == '__main__':

    dict_ = file_dict(*sys.argv)
    hist = histogram(dict_)
    

