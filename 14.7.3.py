
import shelve

def anagram_dict(filE='words.txt'):
    fin=open(filE)
    dicT={} 
    for word in fin:     
        word=word.strip().lower()     
        letters=''.join(sorted(list(word)))       
        dicT.setdefault(letters,[]).append(word)        
    return dicT


def store_anagrams(dicT,filE,flag='n'):    
    db=shelve.open(filE,flag)   
    for letters,words in sorted(dicT.items()):
        if len(words) > 1:
            db[letters]=words          
    db.close()   
    del db
    
def read_anagrams(filE):
    db=shelve.open(filE,'r')   
    for letters in db:
        print letters, ' '.join(db[letters]), '\n'        
    db.close()
    del db
    

if __name__ == '__main__':

    dicT=anagram_dict()
    store_anagrams(dicT,filE='anagrams.db')
    read_anagrams('anagrams.db')
    
