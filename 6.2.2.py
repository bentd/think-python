# Hypotenuse

import math

def hypotenuse():
    print '*'*73,"\nwelcome to dylan's hypotenuse calculator!\n"
    user1=raw_input('what is side a? \n\n')
    user2=raw_input('what is side b? \n\n')
    print 'the hypotenuse of the triangle is: \n\n',math.sqrt(eval(user1+'**2+'+user2+'**2'))
    user3=raw_input('\ndo you wish to finish?\n')
    if user3=='yes': print '\n'; return
    print '\n'
    hypotenuse()

hypotenuse()
