# Chapter 8 Section 7 Exercise 6

# Counter using a search function

import sys

def find(word, letter, start=0):

    if start >= len(word): return -1
    
    while start < len(word):
        if word[start] == letter: return start
        start += 1

    return -1


def count(word, letter):
    count = 0
    index = find(word, letter)
    while index != -1:
        count += 1
        index = find(word, letter, index + 1)
    return count
    
word = '\
Encapsulate this code in a function named count, \
and generalize it so that it accepts the string and \
the letter as arguments.'


def run(name, word= word, letter= 'e'):

        print count(word, letter)


if __name__ == '__main__':

    run(*sys.argv)
