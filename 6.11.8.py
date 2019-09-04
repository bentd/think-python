# Greatest Common Divisor

def gcd(a, b):
    if b>a:
    # print 'Remember, first value must be greater than second value. \n'
        return gcd(b, a)
    #
    elif b==0:
        print 'Greatest Common Divisor is: \n'
        return a
    #
    else:
        r=a%b
        return gcd(b, r)

def run():
    while True:
        print
        print "Welcome to Dylan's GCD (Greatest Common Divisor) Program!\n"
        end='end'
        #
        inputa=input('What is your first number?\n\n')
        if inputa==end:
            return
        #
        print
        inputb=input('What is your second number?\n\n')
        print
        #
        if type(inputa)==int and type(inputb)==int:
            print gcd(inputa, inputb)
            print
            run()
        else:
            print 'Sorry integers only!'
            run()

run()

    
    
