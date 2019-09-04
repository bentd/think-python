# Chapter 8 Section 7 Exercise 5

# Example of a counter program

import sys

def count(word, letter):

    count = 0

    for letters in word:

        if letters == letter: count += 1

    print count


def run(name, word= 'Encapsulate this code in a function named count,\
                    and generalize it so that it accepts the string and\
                    the letter as arguments.', letter= 'e'):

        count(word, letter)


if __name__ == '__main__':

    run(*sys.argv)
