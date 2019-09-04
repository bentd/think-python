# Chapter 11 Section 5 Exercise 6

from time import time
import sys

def fibonacci1(n):
    """ Author """
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

known = {0:0, 1:1}

def fibonacci2(n):
    """ Author """
    if n in known:
        return known[n]

    res = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = res
    return res

def main(name, n= 25, trials= 10):

    if isinstance(n, str): n = int(n)
    if isinstance(trials, str): trials = int(trials)

    average = lambda lis: sum(lis) / len(lis)

    sec1 = []
    
    for trial in range(trials):
        time1 = time()
        fibonacci1(n)
        time2 = time()
        sec1.append(time2 - time1)

    sec1 = average(sec1)
    sec2 = []

    for trial in range(trials):
        time1 = time()
        fibonacci2(n)
        time2 = time()
        sec2.append(time2 - time1)

    sec2 = average(sec2)

    print('The fibonacci sequence without memoization takes about' +
          '{} seconds on average.'.format(sec1) +
          ' While the fibonnacci sequence with memoization takes' +
          ' about {} seconds.'.format(sec2))
        
    
if __name__ == '__main__':

    main(*sys.argv)




        
        

