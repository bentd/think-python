# Srinivasa Ramanujan

from math import *

from sys import *
setrecursionlimit(10000)

def factorial(n):
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result=n*recurse
        return result

def my_pie1(k):
    a=2*(2**0.5)
    b=a/9801.0
    a=0
    for i in range(k):
        c=factorial(4*i)
        d=1103+(26390*i)
        e=(factorial(i))**4
        f=396**(4*i)
        g=c*d
        h=e*f
        j=g/h
        a+=j
    l=b*a
    m=1/l
    return m

def my_pie2(k):
    a=2*(sqrt(2))
    b=a/9801.0
    i=0
    z=0
    while True:
        c=factorial(4*i)
        d=1103+(26390*i)
        e=(factorial(i))**4
        f=396**(4*i)
        g=c*d
        h=e*f
        j=g/h
        z+=b*g/h
        i+=1
        if abs(j)<1e-15: break
    m=1/z
    return m

def author_pie():
    total=0
    k=0
    factor=2*sqrt(2)/9801
    while True:
        num=factorial(4*k)*(1103+26390*k)
        den=factorial(k)**4*396**(4*k)
        term=factor*num/den
        total+=term
        if abs(term)<1e-15: break
        k+=1
    return 1/total

print my_pie1(1000), '\n'
print my_pie2(1000), '\n'
print author_pie(), '\n'
print pi



    
