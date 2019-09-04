# Chapter 10 Section 15 Exercise 12

from sys import *
setrecursionlimit(10000)
from bisect import bisect_left


# Exercise 12


def read_file(filename= 'words.txt'):
    t = []
    fin=open(filename)
    read = fin.read()
    fin.close
    return read.split('\n')

def reverse_pair(lis):
    for word in lis:
        reverse = word[::-1]
        if bisect_left(lis, reverse) >= len(lis): continue
        if lis[bisect_left(lis, reverse)] == reverse: print word, reverse
        

if __name__ == '__main__':

    print bisect_left(read_file(), 'tuba')
    reverse_pair(read_file())
    









        

        
