# Ackermann Function

from sys import *
setrecursionlimit(10000)
# Makes sure the computer doesn't catch fire

def ack(m, n):
    if m==0:
        return n+1
    if m>0 and n==0:
        return ack(m-1, 1)
    if m>0 and n>0:
        return ack(m-1, ack(m, n-1))

def list_ack(a=50, b=50):
    for i in range(a):
        for j in range(b):
            print('ack(',i,',',j,')')
            print(ack(i,j))

def ack_m(x, y):
    for a in [x]:
        for i in range(y):
            print('ack(',a,',',i,')')
            print(ack(a, i))

def ack_test():
    while True:
        end=raw_input('End Function? ')
        if end=='end' or end=='yes':
            break
        else:
            testm=int(input('What is m? '))
            testn=int(input('What is n? '))
            print(ack(testm, testn))

def ack42():
    h=5
    for i in range(65533):
        j=8*(2**i)
        h+=j
    return h



