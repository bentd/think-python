
from math import * 
 
def squareroot(a):
    """ Python Implementation of Newton's Method """
    guess = a / 2.0 
    print guess
    precision = 0.0001
    checker = abs((guess**2) - a)
    while checker > precision:
        guess = (a + a / guess) / 2.0
        print guess
        checker = abs((guess**2) - a)
        print checker
    return guess

squareroot(64)

def run(a): 
  estimate=(a/2.0) 
  while (abs((estimate**2)-a)) > 0.0000001: 
    estimate=(estimate+(a/estimate))*(0.5) 
  return estimate

def comp(a): 
  b=range(a)  
  for i in b: 
    print(i), 
    print(''), 
    print(run(i)), 
    c=((15)-(len(str(run(i)))))
    for k in range(c):
        print(''),
    print(sqrt(i)), 
    d=((15)-(len(str(sqrt(i)))))
    for l in range(d):
        print(''),
    print(''), 
    print(abs((run(i))-sqrt(i))), '\n'
   
comp(101)

print '\n' * 20

print 