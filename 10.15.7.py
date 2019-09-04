# Chapter 10 Section 15 Exercise 7

import sys

def onlyuse(word, letters):
    """
    Function from Chapter 9 Section 2 Exercise 4
    (example of problem recognition)
    """
    truth = True
    for letter in word:
        truth = letter in letters and truth
    return truth

def anagram(word1, word2):
    " Checks if two strings have the same characters... "
    assert isinstance(word1,str) and isinstance(word2,str)
    if onlyuse(word1, word2) and onlyuse(word2, word1): return True
    else: return False

def main(name,word1= 'plea',word2= 'leap', second_example= False):

    print anagram(word1,word2)
    if eval(str(second_example)): print anagram('star','rats')

if __name__ == '__main__':

    main(*sys.argv)



