# Chapter 13 Section 1 Exercise 1

from string import punctuation, whitespace, digits, maketrans, rjust
from random import choice

import sys

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
orig = uppercase + punctuation + digits + whitespace
new = lowercase + ' ' * 48

start = '*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'
end = '*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'

def markov_process(line, dictio, length):
    line = line.strip().split(' ')
    lis = []

    for index in range(len(line) - 2 * length):
        other = index + length
        space = ' '

        a = [line[index + n] for n in range(length)]
        b = [line[other + n] for n in range(length)]

        lis.append((space.join(a), space.join(b)))
      
    for prefix, suffix in lis:
        dictio.setdefault(prefix,set()).add(suffix)
    

def markov_dict(filename,start,end,length):
    openfile = open(filename)
    dictio = {}
    part_of_story = False
    for line in openfile:
        if end in line: part_of_story = False
        if part_of_story: markov_process(line,dictio,length)
        if start in line: part_of_story = True
    return dictio

def random_line(dictio, length= 30):
    string = []
    keys = dictio.keys()
    prefix = choice(keys)
    string.append(prefix)
                   
    for n in range(length):
        while prefix not in dictio: prefix = choice(keys)
        suffix = choice(list(dictio[prefix]))
        string.append(suffix)
        prefix = suffix
                   
    return ' '.join(string)

def main(name, filename= '1661.txt', lon= 5, length= 30, start= start, end= end):

    mark_dict = markov_dict(filename, start, end, lon)
    random_text = random_line(mark_dict, length)

    print ; print random_text ; print

def run():
    main(*sys.argv)
 
if __name__ == '__main__':

    main(*sys.argv)
        
