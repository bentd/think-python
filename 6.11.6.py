#Palindromes
# 11-14-14 16:04 Fixed Bug w/ 'ispalindrome' when I forgot to put elif: palindrome=etc. & return ispalindrome(palindrome)'
# instead I put 'elif: palindrome=etc. & ispalindrome(palindrome)' and I got a None value


def ispalindrome1(m):
    n=m[::-1]
    if m==n:
        return True
    else:
        return False

while True:
    test=raw_input('Palindrome Test: What is the word? ')
    if test=='end':
        break
    print(ispalindrome(test))


def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
def ispalindrome2(palindrome):
    if len(palindrome)==0:
        return True
    elif first(palindrome)==last(palindrome):
        return ispalindrome(middle(palindrome))
    else:
        return False

def run():
    while True:
        print
        print "Welcome to Dylan's Palindrome1 Calculator! \n"
        inputa=raw_input('What word would you like to test? \n\n')
        print
        end=['end', 'done']
        if inputa in end:
            return
        else:
           print ispalindrome(inputa), '\n\n'
    return

run()
















# Author
__________________________________________________________________________-

def ispalindrome2(word):
    """ Author Point Out That Is_Reverse Had Applications For Is_Palindrome
        This Is Known As Problem Recognition """

    def is_reverse2(word1, word2):
        if len(word1)!=len(word2): return False
        i,j=0,-1
        while j>=-1*len(word2):
            if word1[i]!=word2[j]: return False
            i+=1
            j+=-1
        return True

    return is_reverse2(word, word)

