# Chapter 10 Section 8 Exercise 6


def is_sorted(t):

    for i in range(len(t) - 1):
        if t[i] > t[i + 1]: return False
    else: return True

if __name__ == '__main__':
    
    print is_sorted(['a','l','c'])


