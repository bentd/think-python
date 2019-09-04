# Chapter 8 Section 13 Exercise 11

# All seem to have some form of semantic error except for any_lowercase4

a = 'JohnD'

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print 1
print any_lowercase1(a)
print

print 2
print any_lowercase2(a)
print type(any_lowercase2(a))
print

print 3
print any_lowercase3(a)
print

print 4
print any_lowercase4(a)
print

print 5
print any_lowercase5(a)
print
