# RSA Encryption Program

import threading

from random import randint
from string import join

from sys import *
setrecursionlimit(1000000000)


def generate():
    """
    Generates a modulus, encryption key, and decryption key for user
    Beware this overwrites any file named rsa.keys that already exists
    i.e. from previous RSA key generations
    
    """

    level=raw_input('Choose the level of the encryption (in average bit-length): 7-bit, 9-bit, 11-bit, 13-bit, 15-bit, 19-bit, or 25-bit? ')
    print

    def prime(level='7-bit'):
        """ Returns a random prime integer """
        
        level = level.lower()
        if level == '7-bit': prime1 = randint(21,99)
        elif level == '9-bit': prime1 = randint(101,499)
        elif level == '11-bit': prime1 = randint(501,1999)
        elif level == '13-bit': prime1 = randint(2001,9999)
        elif level == '15-bit': prime1 = randint(10001,49999)
        elif level == '19-bit': prime1 = randint(100001,499999)
        elif level == '25-bit': prime1 = randint(10000001,49999999)

        def isPrime(a):
            """
            StackOverflow (brock west)
            Tests an integer to prove it's prime

            """
            return not ( a < 2 or any(a % i == 0 for i in range(2, int(a ** 0.5) + 1)))
        
        if not isPrime(prime1): return prime(level) 
        return prime1
    
    prime1, prime2 = prime(level), prime(level)
    modulus = prime1 * prime2
    phi_of_modulus = (prime1-1)*(prime2-1)

    def keys(totient):
        """ Allows user to decide which pair of keys to use out of a list and returns e/d key in list """
        
        keys=[[e,(k*totient+1)/e] for k in range(1,11) for e in range(2,int((k*totient+1)**(0.5)+1)) if (k*totient+1)%e == 0]
        index=0
        for pair in keys: print str(index).rjust(2), pair; index+=1
        print
        user=input('Which encryption/decryption key pair would you like? ')
        return keys[user]

    
    kept=keys(phi_of_modulus)
    e,d=kept[0],kept[1]
    
    print1='\nYour prime factors are: '+str(prime1)+' and '+str(prime2)+'\n'
    print2='Your public modulus is: '+str(modulus)+' and the phi of the modulus is: '+str(phi_of_modulus)+'\n'
    print3='Your public encryption key is: '+str(e)+' and your private decryption key is: '+str(d)+'\n'
    
    fin=open("rsakeys.txt",'w')
    fin.write(print1+print2+print3)
    print print1,print2,print3

    

def userencrypt():
    """
    Encrypts the user's message with a provided
    public modulus and encryption key
    
    """

    e=input('What is the public encryption key?\n')
    modulus=input('What is the public modulus?\n')

    prompt1='\nIf you wish to copy your plaintext message to the plaintext.txt file \nbefore encryption, copy message to file, save, then enter "file"\n\n'
    prompt2='Or if you wish to enter your plaintext message in-program, enter "program"\n\nAnswer: '
    user=raw_input(prompt1+prompt2)

    if user == 'file':fin=open("plaintext.txt", 'r');plaintext=fin.read()
    if user == 'program':plaintext=raw_input('\nWhat is the message? ');fin=open("plaintext.txt",'w');fin.write(plaintext);fin.close()    

    def encrypt(message,e,modulus):
        cypher=[]
        for character in message:
            cypher+=[((ord(character))**e)%modulus]
        return cypher

    ciphertext=encrypt(plaintext,e,modulus)
    fin=open("ciphertext.txt",'w')
    for number in ciphertext: fin.write(str(number)+'\n')
    fin.close()
    print '\nThis is your encrypted message:  \n\n',ciphertext,'\n'



def userdecrypt():
    d=input('What is your private decryption key?\n')
    modulus=input('What is the public modulus?\n')

    prompt1='\nIf you wish to copy your ciphertext message to the ciphertext.txt file \nbefore decryption, copy message to file, save, then enter "file"\n\n'
    prompt2='Or if you wish to enter your cipher message in-program, enter "program"\n\nAnswer: '
    user=raw_input(prompt1+prompt2)

    if user == 'file':fin=open("ciphertext.txt", 'r');ciphertext=fin.read()
    if user == 'program':
        ciphertext=input('\nList the codes of the message, separated by commas. ')
        fin=open("ciphertext.txt",'w')
        for number in ciphertext: fin.write(str(number)+'\n')
        fin.close()  

    def decrypt(cypher,d,modulus):
        message=[]
        for code in cypher:
            message+=[chr((code**d)%modulus)]
        return join(message,'')

    def text(file1):
        fin=open(file1)
        data=[]
        for line in fin:
            data+=[int(line.strip())]
        return data

    plaintext=decrypt(text("ciphertext.txt"),d,modulus)
    fin=open("plaintext.txt", 'w')
    fin.write(plaintext)
    fin.close()
    print '\nThis is your decrypted message: \n\n',plaintext,'\n'



def run():

    """ Executes program """
    
    while True:
        welcome="Welcome to Dylan's RSA Encryption Program!\n\n"
        prompt='Please select one of the following (if you wish to quit, type \"quit"):\n\n'
        a='a Do You Wish To Generate RSA Keys?\n'
        b='b Do You Wish To Encrypt A Plaintext Message?\n'
        c='c Do You Wish To Decrypt A Ciphertext Message?\n\n'
        fin1=open("plaintext.txt",'a')
        fin2=open("ciphertext.txt",'a')
        fin3=open("rsakeys.txt",'a')
        [fil.close() for fil in [fin1,fin2,fin3]]
        option=raw_input(welcome+prompt+a+b+c).lower(); print
        if 'quit' in option: break 
        command={'a':generate,'b':userencrypt,'c':userdecrypt}
        command[option]()
        print '>>> ================================ RESTART ================================\n>>>\n'
    else: return


if __name__ == '__main__':

    lock = threading.Lock()
    lock.acquire()
    run()
    lock.release()
    
    # this portion of the code deletes unwanted files

    from os import remove

    delete=raw_input('Do you wish to delete rsakeys.txt? ')
    if delete.lower() == 'yes': 
        remove("rsakeys.txt")

    delete=raw_input('Do you wish to delete plaintext.txt? ')
    if delete.lower() == 'yes':
        remove("plaintext.txt")

    delete=raw_input('Do you wish to delete ciphertext.txt? ')
    if delete.lower() == 'yes':
        remove("ciphertext.txt")







    



