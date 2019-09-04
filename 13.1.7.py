# Chapter 13 Section 1 Exercise 1

from string import punctuation, whitespace, digits, maketrans, rjust
from random import choice, randint
from bisect import bisect_left

import sys

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
orig = uppercase + punctuation + digits + whitespace
new = lowercase + ' ' * 48

start = '*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'
end = '*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'
 
count = 0

def process_line(line, hist):
    
    """ Analyzes one line of the text: mapping each word with how many times it appears in the text
        (Has to edit the line to get rid of anything that is not a word) """

    # No need for return statement in process_line because you are editing the dictionary
    # itself not a copy of the dictionary...

    global orig, new, count
    trans = maketrans(orig, new)
    line = line.translate(trans).split()

    for word in line:
        
        count = count + 1
        hist[word] = hist.get(word, 0) + 1

def process_text(filename, start, end):
    
    """ Analyzes text and returns a histogram (type dictionary)
        mapping each word to it's frequency within the text """
    
    openfile = open(filename)
    part_of_story = False
    hist = dict()
    
    for line in openfile:
        
        if end in line: part_of_story = False
        if part_of_story: process_line(line, hist)
        if start in line: part_of_story = True
    
    return hist


def cumu(t):
    """ Returns a new list with each number equal to the sum of
        the numbers in the old list before it (cumulative sum) """
    s = t[:] ; p = []
    while len(s) > 0:
        p.append(sum(s))
        s=s[:len(s)-1]
    return p[::-1]

def main(name, filename= '1661.txt', start= start, end= end):

    global count

    frequencies = process_text(filename, start, end)

    lis = sorted([(num, word) for word, num in frequencies.items()])

    sums = cumu(frequencies.values())

    rand = randint(1, sums[-1])

    index = bisect_left(sums, rand)

    print '\n\nNow for a random word.\n' 

    word = lis[index][1]

    print word, str(frequencies[word]) + '/' + str(count), '{:%}'.format(1.0 * frequencies[word] / count)

    print ; print

def run():

    main(*sys.argv)
 
if __name__ == '__main__':

    main(*sys.argv)
        
