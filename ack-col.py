# Ackermann-Collatz Program

# Collatz Conjuction - Via division, multiplication, and addition it always leads to 1
# Ackermann Function - Creates large values with small integers via non-primitive recursion

# Finding the Collatz Conjecture of the Ackermann Function of 4 and 2
# A(4,2) -- > 19,729 digits long

from sys import *
setrecursionlimit(100000)

def ack42():
    h=5
    for i in range(65533):
        j=8*(2**i)
        h+=j
    return h

print(ack42())
print
print
print('len of ack42 is: ', len(str(ack42())))
print
print

def sequence(n):
    while n!=1:
        print n
        if n%2==0:
            n=n/2
        else:
            n=n*3+1

sequence((ack42()))


