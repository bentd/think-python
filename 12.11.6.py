# Reducible


word='sprite'

from random import randint


def dictionary(file1='words.txt'):

    fin=open(file1)
    dictionary={}

    for words in fin:
        dictionary[words.strip()]=words.strip()

    dictionary['a']='a'
    dictionary['i']='i'
    dictionary['']=''

    return dictionary


def simple_reduce(word):

    children=[]
    word1=list(word)

    for index in range(len(word)):
        
        word1.pop(index)
        children.append(''.join(word1))
        word1=list(word)

    return children
    

dict_=dictionary()
list_=sorted(dict_.keys())

memo_true={}
memo_false={}


def boolean_reduce(word):

    if word == '': return True

    global dict_
    global memo_true
    global memo_false
    
    if word in memo_false or not word in dict_: return False
    if word in memo_true and word in dict_:  return True
  
    reduced_words=[]
    for child in simple_reduce(word):
        if child in dict_: reduced_words.append(child)
        
    if len(reduced_words) == 0:
        memo_false[word]=word
        return False
       
    truth=[]
    for words in reduced_words:
        truth.append(boolean_reduce(words))

    if True in truth: memo_true[word]=word; return True
    else: return False


def reduce_word(word):

    global dict_
    word_list=[word]

    while len(word) > 0:
        
        list_=[child for child in simple_reduce(word) if boolean_reduce(child) == True]
        del child 
        word=list_[randint(0, (len(list_)-1))]
        word_list.append(word)

    return word_list

def DSU(list_, stop=len(list_)):

    new=[(len(item[0]),)+item for item in list_]
    new.sort(reverse=True)
    newer=[item2 for item0, item1, item2 in new[0:stop]]
    return newer
        

def print_reducibles():

    global dict_
    global list_

    dict__=dict()

    for word in list_:
        if not boolean_reduce(word): continue
        dict__[word]=reduce_word(word)
        
    tuple_list=DSU(sorted(dict__.items()), stop=5)

    for word_list in tuple_list:
        for word in word_list: print word,
        print

    return

print_reducibles() 

        

        
