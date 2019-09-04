# Chapter 9 Section 2 Exercise 4

import sys
import os.path as path

def onlyuse(word, letters):
    " Makes sure the word has letters only within the set of 'available' letters "
    truth = True
    for letter in word:
        truth = letter in letters and truth
    return truth


def sentence(filename, letters):

    " Helps user to make a sentence with words that only use letters in a specific set of 'letters' "

    text = open(filename)
    lis = []
    for line in text:
        line = line.strip()
        if onlyuse(line, letters): lis.append(line)
    text.close()
    print 'The available words that only use the letter(s) %s include: \n' %letters
    for line in lis:
        print line,

def run(name, filename= 'words.txt', letters= 'acefhlo'):

    assert path.isfile(filename)

    sentence(filename, letters)

if __name__ == '__main__':

    run(*sys.argv)
