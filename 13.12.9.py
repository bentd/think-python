# Zipf Analysis Program - Opens Text and Runs Zipf Algorithm On That Text - Think Python Excercise
# Partly based on Allen B. Downy (Author) code...


from string import punctuation, digits, whitespace, maketrans, translate

import numpy as np

import matplotlib.pyplot as plt

import sys


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
orig = uppercase + punctuation + digits + whitespace
new = lowercase + ' ' * 48
 
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



def frequency_rank(hist):

    " Takes a histogram made by process_text and returns a list of tuples, each containing the frequency of a word paired with the word's rank "

    # Could use enumerate...

    frequencies = sorted(hist.values(), reverse = True)
    ranks = range(1, len(frequencies) + 1)
    return ranks, frequencies



def plot_loglog(fr_list):

    " Using matplotlib, it plots log frequency vs log rank on a chart "

    x = np.array(fr_list[0])
    y = np.array(fr_list[1])

    plt.figure(1)
    plt.xlabel('Word Rank')
    plt.ylabel('Word Frequency')
    plt.title('Zipf Analysis - loglog')
    plt.loglog(x, y)



def plot_scatter(fr_list):

    " Using matplotlib, it plots frequency vs rank on a chart "

    x = np.array(fr_list[0])
    y = np.array(fr_list[1])

    plt.figure(2)
    plt.xlabel('Word Rank')
    plt.ylabel('Word Frequency')
    plt.title('Zipf Analysis - scatter')
    plt.plot(x, y, 'go')
    plt.show()
    


def find_slope(fr_list):

    x = np.log10(fr_list[0])
    y = np.log10(fr_list[1])

    slope, intercept = np.polyfit(x, y, 1)
    # ^ Solution found on Stack Overflow
    print '\n\nThe slope of the frequency vs rank plot (s) is %f.\n\nWhile the intercept is %f.\n' % (slope, 10**intercept)
    


def main(name, filename = '1661.txt', scatter = 'False', start = '*** START OF THIS PROJECT GUTENBERG EBOOK', end = '*** END OF THIS PROJECT GUTENBERG EBOOK'):

    hist = process_text(filename, start, end)
    fr_list = frequency_rank(hist)
    find_slope(fr_list)
    plot_loglog(fr_list)
    if eval(scatter): plot_scatter(fr_list)
    else: plt.show()



if __name__ == '__main__':

    main(*sys.argv)

    



