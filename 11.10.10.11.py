def read_dictionary(filename='c06d.sdx'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

d = read_dictionary()

# Rotate Pairs

fil=open('words.txt')

fin={}
num=0

for word in fil:
    fin[word.strip()]=num
    num+=1

def rotate_letter(letter, n):
    """
    Author
    Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    """
    Author
    Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

file1=open('pairs.txt','w')

def find2(fi):
    for word in fi:
        for num in range(1,26):
            if rotate_word(word,num) in fi:
                file1.write(word+' '+rotate_word(word,num)+' '+str(num)+'\r\n')
        
find2(fin)

fil=open('homophone.txt','w')

def homophone():
    for word in fin:
        if len(word) is 5:
            word1=word[1:]
            word2=word[0]+word[2:]
            try:
                if d[word]==d[word1]==d[word2]:
                    fil.write(word+' '+word1+' '+word2+'\r\n')
                    print word,'',word1,'',word2
            except KeyError:
                continue

homophone()
