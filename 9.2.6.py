# Chapter 2 Section 2 Exercise 6

import sys

def is_abecedarian(word):

    " Tests a word to make sure its letters are in alphabetical order "

    word = word.lower()
    end = len(word) - 1 
    index = 0
    
    while index < end:
        letter1 = word[index]
        letter2 = word[index + 1]
        if not ord(letter1) <= ord(letter2): return False
        index += 1
        
    return True

def run(name, filename= 'words.txt'):

    " Processes a file and prints any line whose letters are in alphabetical order "
    
    text = open(filename)

    for line in text:

        if is_abecedarian(line): print line,

    text.close()


if __name__ == '__main__':

    run(*sys.argv)

        

        
