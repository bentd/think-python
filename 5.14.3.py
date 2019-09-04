# -*- coding: cp1252 -*-

# Fermat’s Last Theorem says that there are no positive integers a, b,and c
# such that a^n + b^n = c^n for any values of n greater than 2.

def fermat1(a,b,c,n):
    x=(a**n)+(b**n)
    y=(c**n)
    if x==y:
     print('Holy Smokes, Fermat was wrong! ')
    else:
     print ('Nevermind, he was right.')
fermat(2,3,4,2)


def fermat(p, r=11):
    a=list(range(1, r))
    b=[]
    c=[]
    d=[]
    for i in a:
        i=i**p
        b.extend([i])
        c.extend([i])
        d.extend([i])
    h=raw_input('P='+str(p)+' Find all iterations or just those that are equal?: ')
    if h=='equal' or h==' equal':
        for s in b:
            for t in c:
                for u in d:
                    if (s+t)==u and u>1 and p<3:
                        print('Fermat was right!, True',(s**(1.0/p)),'^',p,'+',(t**(1.0/p)),'^',p,'=',(u**(1.0/p)),'^',p)
                    elif (s+t)==u and u>1 and p>2:
                        print('Holy Smokes! Fermat was wrong, True',(s**(1.0/p)),'^',p,'+',(t**(1.0/p)),'^',p,'=',(u**(1.0/p)),'^',p)
    else:
        for s in b:
            for t in c:
                for u in d:
                    if (s+t)==u and u>1 and p<3:
                        print('Fermat was right!, True',(s**(1.0/p)),'^',p,'+',(t**(1.0/p)),'^',p,'=',(u**(1.0/p)),'^',p)
                    elif (s+t)==u and u>1 and p>2:
                        print('Holy Smokes! Fermat was wrong, True',(s**(1.0/p)),'^',p,'+',(t**(1.0/p)),'^',p,'=',(u**(1.0/p)),'^',p)
                    else:
                        print('Nevermind Fermat was right, False',(s**(1.0/p)),'^',p,'+',(t**(1.0/p)),'^',p,'!=',(u**(1.0/p)),'^',p)

def repetition(x=11, y=101, f=fermat):
    e=list(range(2, x))
    for i in e:
        f(i, y)

def fermats(m, n, o, p=2):
    if ((m**p)+(n**p))==(o**2) and p>2:
        print('Fermat was right')
    elif ((m**p)+(n**p))==(o**2) and p<3:
        print('Hoky Smokes,  Fermat was wrong!')
    else:
        print('Nevermind Fermat was right')

def fermatss(a,b,c,n):
    x=(a**n)+(b**n)
    y=(c**n)
    if x==y:
     print('Holy Smokes, Fermat was wrong! ')
    else:
     print ('Nevermind, he was right.')

repetition(11, 51)

