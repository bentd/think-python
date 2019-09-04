# Chapter 9 Section 2 Exercise 2

# Program reads a file and prints any line that does not contain the provided letter
# Also prints the percentage of lines that do not the provided letter

import sys

def has_no_letter(filename, letter, print_= False):
    """ Counts and finds words within file that do not have the 'default' letter """

    assert type(letter) is str
    fin = open(filename)
    ratio = [0,0]
    
    for line in fin:       
        line = line.strip()
        ratio[1] += 1
        
        if letter not in line and print_:
            ratio[0] += 1
            print line,
            
        elif letter not in line and not print_:
            ratio[0] += 1

    percentage = 1.0 * ratio[0] / ratio[1]
    
    print('\n\n\n' + 
          'The percentage of words within document that do not contain the ' + 
          'letter {} is {:.3%}.'.format(letter, percentage))



def run(name, filename= 'words.txt', letter= 'e', print_= False):

    if type(print_) is str: print_ = eval(print_)

    has_no_letter(filename, letter, print_)


if __name__ == '__main__':

    run(*sys.argv)
