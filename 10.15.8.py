# Chapter 10 Section 15 Exercise 8

from random import randint
import sys

def has_duplicates(t):
    for i in range(len(t)-1):
        char = t.pop(i)
        if char in t: return True
        t[i:i] = [char]
    else: return False

def print_duplicates(t):
    for i in range(len(t)-1):
        char = t.pop(i)
        if char in t: print char
        t[i:i] = [char]
    else: return None

def count_duplicates(t):
    count = 0
    for i in range(len(t)-1):
        char = t.pop(i)
        if char in t: count += 1
        t[i:i] = [char]
    else: return count

def birthday_paradox(num):
    dates = []
    
    for person in range(num):
        dates.append(randint(1,365))
        
    truth = has_duplicates(dates)
    
    return truth

def birthday_paradox_percentages(tries, num_of_people):
    counts = [0,0]
    
    for try_ in range(tries):
        if birthday_paradox(num_of_people):
            counts[0] += 1
            counts[1] += 1
        else:
            counts[1] += 1
        
    return 1.0 * counts[0] / counts[1]

def main(name, num_of_people= 23, trials= 1000):
    
    lis = [1, 5, 9, 7, 1, 6, 7]

    print has_duplicates(lis); print

    num_of_people = int(num_of_people)
    trials = int(trials)

    print('A quick experiment shows that in a room of {} people, '.format(num_of_people) +
          'it is {} '.format(birthday_paradox(num_of_people)) + 
          'likely that at least two people share the same birthday.')

    print 

    print('Yet a complete experiment shows in a room of {} people, '.format(num_of_people) +
          'that their is {:.2%}'.format(birthday_paradox_percentages(trials, num_of_people)) +
          ' likelihood that at least two people share the same birthday.')

    print 

if __name__ == '__main__':

    main(*sys.argv)


