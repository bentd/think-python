# Chapter 11 Section 10 Exercise 9

def histogram(s): 
    """ Exercise 2 """
    d = dict() 
    for c in s: 
        d[c] = d.get(c,0) + 1
    return d

def has_duplicates(s):
    """ Exercise 11.10.9 """
    lis = histogram(s)
    for i in lis:
        if lis[i] > 1: return True
    else: return False

if __name__ == '__main__':
    
    test56 = ['a','b','t','b','e','l','k']
    print has_duplicates(test56)





        
        

