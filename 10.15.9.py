# Chapter 10 Section 15 Exercise 9

import sys
from copy import copy
    
def remove_duplicates(t):
    s = copy(t)
    index = 0
    while index < (len(s)):
        char = s.pop(index)
        if char not in s: s[index:index] = [char]; index += 1
    return s

if __name__ == '__main__':
    
    t = [1,2,2,3,4,4,6,8,8,8]
    s = remove_duplicates(t)

    print t
    print s

