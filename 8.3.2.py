# -*- coding: cp1252 -*-

# Chapter 8 Section 3 Exercise 2

# Abecedarian Series (Alphabetical Order)

# In Robert McCloskey’s book Make Way for Ducklings,
# the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack

def ducks():
    letters = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in letters:
        if letter in ['O','Q']: letter += 'u'
        print letter + suffix
    return

if __name__ == '__main__':

    ducks()
