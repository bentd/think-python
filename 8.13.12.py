# ROT13

# MY VERSION

print

def run():
    """ Author Pointed Out The Use of %26 Which I Incorporated Into My Own Function """
    done='done'
    rotation=input('By what integer would you like to rotate your input value? \n\n')
    if rotation == done: return
    if rotation > 0: rotation=rotation%26
    else: rotation= rotation%-26
    print
    print '*'*77, '\n'
    print "Welcome to Dylan's ","ROT"+str(rotation)," Encoder! \n"
    print 
    while True:
        inputa=raw_input('What would you wish to encode? \n\n')
        if inputa == 'done': break
        if inputa == 'change rotation':
            print '\n\n', '='*77, '\n\n'
            run()
        initial=''
        for i in inputa:  
            if ord(i) > 64 and ord(i) < 91:
                if ord(i)+rotation >= 91:
                    rotate=64+(rotation-(90-ord(i)))
                    i=chr(rotate)
                    initial+=i   
                elif ord(i)+rotation < 65:
                    rotate=91+(rotation+(ord(i)-65))
                    i=chr(rotate)
                    initial+=i                    
                else:
                    i=chr(ord(i)+rotation)
                    initial+=i                    
            elif ord(i) > 96 and ord(i) < 123:                
                if ord(i)+rotation >= 123:
                    rotate=96+(rotation-(122-ord(i)))
                    i=chr(rotate)
                    initial+=i
                elif ord(i)+rotation < 97:
                    rotate=123+(rotation+(ord(i)-97))
                    i=chr(rotate)
                    initial+=i                    
                else:
                    i=chr(ord(i)+rotation)
                    initial+=i                    
            else:
                initial+=i                
        print initial, '\n'
    print
    return

run()
print



