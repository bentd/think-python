# Collatz Conjecture

def sequence(n):
    while n!=1:
        print n
        if n%2==0:
            n=n/2
        else:
            n=n*3+1

def user():
    while True:
        print
        print("Welcome to Dylan's Collatz Calculator!")

        print
        end='end'

        u=input('What is your number? ')
        if u==end:
              return

        print
        if type(u)==int:
              sequence(u)
              print
              user()

        else:
              print 'Sorry integers only!'
              user()

user()
