# Chapter 10 Section 15 Exercise 10


# NEW HYPOTHESES
# filelist2 may be slower due to the fact that it is creating
# an entirely new list object in each iteration
# meaning that the program is making multiple list objects

# which is why filelist1 is much faster as the function only works with one file object

# its interesting to note that filelist2 is actually faster when reading only a few lines to a few hundred lines
# after about 400 lines filelist1 becomes faster


# OLD HYPOTHESIS
# filelist3 may be faster as you are finding the end of the list
# significantly faster using len function

# my hypothesis for function filelist2's slow computation is due to the fact that the function has to find
# the end of the list each time it updates it



import sys
from time import time
from os.path import isfile
import string


def timetest1():
    time1 = time()
    t = ['a','p','p','l']
    t.append('e')
    time2 = time()
    return 'timetest1 (append) in: %s secs' % str(time2 - time1)

def timetest2():
    time1 = time()
    t = ['a','p','p','l']
    t = t + ['e']
    time2 = time()
    return 'timetest2 (t = t + [?]) in: %s secs' % str(time2 - time1)

def filetime1(file_= 'words.txt', num= 50):
    time1 = time()
    t = list()
    
    with open(file_) as fin:
        length = sum(1 for line in fin)
    if length < num: num = length

    fin = open(file_)
    
    for n in range(num):
        t.append(fin.readline().strip())
    time2 = time()
    return 'filetime1 (append) in: %s secs' % str(time2 - time1)

def filetime2(file_= 'words.txt', num= 50):
    time1 = time()
    t = list()

    with open(file_) as fin:
        length = sum(1 for line in fin)
    if length < num: num = length

    fin = open(file_)
    
    for n in range(num):
        t = t + [fin.readline().strip()]
    time2 = time()
    return 'filetime2 (t = t + [?]) in: %s secs' % str(time2 - time1)

def filetime3(file_= 'words.txt', num= 50):
    time1 = time()
    t = list()

    with open(file_) as fin:
        length = sum(1 for line in fin)
    if length < num: num = length

    fin = open(file_)
    
    for n in range(num):
        t[len(t) : len(t)] = [fin.readline().strip()]
    time2 = time()
    return 'filetime3 (t[len(t) : len(t)] = [?]) in: %s secs' % str(time2 - time1)

def main(name, filename= 'words.txt', num= 400):

    assert isfile(filename)
    num = int(num)

    print timetest1()
    print timetest2()
    print filetime1(filename, num)
    print filetime2(filename, num)
    print filetime3(filename, num)


if __name__ == '__main__':

    main(*sys.argv)





        

        
