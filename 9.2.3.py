# Chapter 9 Section 2 Exercise 3
# Reads a file and computes the number of lines within file do not contain a set of provided letters

import sys
import os.path as path

def forbidden(forbid):
    " Creates a list of forbidden letters "
    
    forbid = forbid.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    setlist = ''
    for letter in alphabet:
        if letter not in forbid: setlist += letter
    return setlist


def avoids(word, letters):
    " Tests whether a word contains any of the forbidden letter "
    
    for letter in letters:
        if letter in word: return False
        else: continue
    else: return True

def avoids_count(filename):
    """ Counts and returns the number of lines within a document
        that do not contain forbidden letters
        n: numerator
        d: denominator
    """
    
    text = open(filename)   
    letters = raw_input(
        "\nwhat are the letters you wish to avoid?\n" +
        "these are your 'forbidden' letters\n\n")
    
    (n,d)=(0,0)
    for line in text:
        line = line.strip()
        if not avoids(line, letters): d += 1
        if avoids(line, letters): n += 1; d += 1

    text.close()
    print("\n{} lines out of {} lines within document".format(n, d) +
          " avoid the letters '{}'. ".format(letters) + 
          "(Percentage {:.2%})".format(1.0 * n / d))


def run(name, filename= 'words.txt', continue_ = True):

    assert path.isfile(filename)
          
    while continue_:
          avoids_count(filename)
          continue_ = raw_input('\ncontinue the program? ')
          if continue_.lower() is 'yes': continue_ = True
        
if __name__ == '__main__':

          run(*sys.argv)
