# Chapter 13 Section 1 Exercise 1

from string import punctuation, whitespace, digits, maketrans, ljust, rjust

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

def most_frequent(hist, n=20):
    
    " Converts text histogram (dictionary) into list of words in order by their frequency within the text "
    
    lis = []
    for item in hist.items():
        lis.append(item[::-1])
    lis.sort(reverse= True)
    return lis[:n]

def main(name, filename= '1661.txt', start= start, end= end, n=20):

    frequencies = process_text(filename, start, end)

    print('\n\nThere are %d words in this text.' % len(frequencies) +
	  '\n\n' + 
	  'The most used words include:' +
	  '\n')

    most_used_words = most_frequent(frequencies, n)

    for freq, word in most_used_words:
        print ljust(word, 7) + rjust(str(freq), 5)

    print; print
 
if __name__ == '__main__':

    main(*sys.argv)
        
