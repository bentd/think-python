# Car Talk 1 Puzzle: Words w/ 3 Consecutive Double Letters


def test(word, count=0):
    """ Stole Author's format from previous program:
        Create a recursive function in which lowers the value of one of its parameters
        until a base case is reached.
    """
    if count>1: return True        
    elif len(word)<4: return False        
    elif word[0]==word[1]!=word[2]==word[3]: return test(word[2:], count+1)    
    else: return test(word[1:], count)
    
def dicti():
    fin=open ("words.txt")
    print '\n\n','Here are the words that contain 3 consecutive double letters: \n\n'
    for word in fin:
        if test((word.strip())): print (word.strip()),'', ; continue
        else: continue
    else: print '\n\n'

dicti()



# Author
#_______________________________________________________________________________

def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
       Author found one my bugs which was that I did not think to
       reduce the count to zero if a condition came back false.
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print word


print 'Here are all the words in the list that have'
print 'three consecutive double letters.'
find_triple_double()
print ''




# Drafts
#_______________________________________________________________-
    
def cartalk1(word):
    word, value, count=word.strip(), 0, 0
    while value < len(word):
        if count > 2: return True
        if value==len(word)-2 and word[value]==word[value+1]: count+=1;value+=1; continue
        if word[value]==word[value+1] and word[value]!=word[value+2]: count+=1;value+=1; continue
        value+=1
    else: return False

def cartalk2(word):
    word=word.strip()
    count,value=0,0
    if word[-1]==word[-2]: count+=1
    for i in word:
        if count<2: return True
        if value==len(word)-1: break
        if i[value]==value[value+1]: count+=1; value+=1; continue
        else: value+=1; continue
    else: return False



def cartalk3(word):
    # word=word.strip()
    value=0
    while value < len(word):
        try:
            if word[value]==word[value+1]:
                if word[value+1]!=word[value+2]==word[value+3]:
                    if word[value+3]!=word[value+4]==word[value+5]: return True
        except IndexError:
            value+=1
    else: return False    
    
