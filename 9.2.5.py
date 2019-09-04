# Chapter 9 Section 2 Exercise 5

import sys
from os.path import isfile

def onlyuse(word, letters):
    """ Makes sure the word has letters only within the set of 'available' letters """
    truth = True
    for letter in word:
        truth = letter in letters and truth
    return truth

def useall_prob_recognition(word, letters):

    # Example of problem recognition as onlyuse and useall perform same operations and can be refactored
    return onlyuse(letters, word)

def useall(word, letters):
    """ Makes sure that each required letter corresponds to atleast one other letter
        within the word, in other words that all 'required' letters are used
    """
    truth = True
    for letter in letters:
        truth = letter in word and truth
    return truth

def run(name, filename= 'words.txt', letters= 'aeiouy'):

    assert isfile(filename)

    print "Here are some lines within file {} that do not contain letters '{}': \n".format(filename, letters)

    with open(filename) as text:

        for line in text:
            line = line.strip()
            if useall(line, letters): print line,

if __name__ == '__main__':

    run(*sys.argv)
            
