# Chapter 8 Section 6 Exercise 4

# Example of a search using string traversal

import sys

def find(word, letter, start=0): 
    while start < len(word):
        if word[start] == letter: return start
        start += 1
    return -1

def run(name, word= 'The Love Spell Potential', letter= 'S', start= 0):

    print 'Word is: ' + word
    print 'Letter is: ' + letter
    
    index = find(word,letter,start)
    if not index == -1: print letter + ' was found in index ' + str(index) + ' of "' + word +'".'

if __name__ == '__main__':

    run(*sys.argv)
