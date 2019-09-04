# Chapter 11 Section 5 Exercise 7

import sys
sys.setrecursionlimit(5000)

known = {'0-0':1}

strings = lambda x,y: str(x) + '-' + str(y)

def ackermann(m, n):
    
    string = strings(m,n)
    
    if string in known: return known[string]
    
    if m == 0:
        known[string] = n + 1
        return n + 1
    
    if m > 0 and n == 0:
        re = ackermann(m-1, 1)
        known[string] = re
        return re
    
    if m > 0 and n > 0:
        re = ackermann(m-1, ackermann(m, n-1))
        known[string] = re
        return re

print ackermann(3,6)
print ackermann(3,7)
print ackermann(3,8)
print ackermann(3,9)
print ackermann(3,10)
print known







        
        

