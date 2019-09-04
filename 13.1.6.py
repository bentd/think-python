# Chapter 13 Section 1 Exercise 1

from string import punctuation, whitespace, digits, maketrans, rjust

import sys

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
orig = uppercase + punctuation + digits + whitespace
new = lowercase + ' ' * 48

start = '*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'
end = '*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'
 
def process_line(line, hist):
    
    """ Analyzes one line of the text: mapping each word with how many times it appears in the text
        (Has to edit the line to get rid of anything that is not a word) """

    # No need for return statement in process_line because you are editing the dictionary
    # itself not a copy of the dictionary...

    global orig, new
    trans = maketrans(orig, new)
    line = line.translate(trans).split()

    for word in line:
        
        hist[word] = hist.get(word, 0) + 1

def process_text(filename, start, end):
    
    " Analyzes text and returns a histogram (type dictionary) mapping each word to it's frequency within the text"
    
    openfile = open(filename)
    part_of_story = False
    hist = dict()
    
    for line in openfile:
        
        if end in line: part_of_story = False
        if part_of_story: process_line(line, hist)
        if start in line: part_of_story = True
    
    return hist

def process_dictionary(filename):
    
    dicti = {}
    openfile = open(filename)
    
    for word in openfile:
         dicti[word.strip()] = 1
         
    return dicti


def main(name, dictname= 'words.txt', filename= '1661.txt', start= start, end= end):

    frequencies = process_text(filename, start, end)

    dictionary = set(process_dictionary(dictname))

    undefined = set(frequencies) - dictionary

    print('\n\nThere are %d words in this text.' % len(frequencies) +
          ' Here are some that are not included within the provided dictionary.\n\n')

    for word in sorted(list(undefined)):
        print word, frequencies[word]

    print; print
 
if __name__ == '__main__':

    main(*sys.argv)
        
