# Anagrams
# takes a few hints from author

def anagram_dict(file1='words.txt'):

    file1=open(file1)
    anagram_dict={}

    for word in file1:
        word=word.strip().lower()
        letters=tuple(sorted(list(word)))
        anagram_dict.setdefault(letters,[]).append(word)

    else: return anagram_dict

def anagrams(bingo=False, dict1=anagram_dict(), n=8, d=1, print1=True):

    if bingo:
        anagram_words=[words for letters, words in dict1.items() if len(words) > d if len(letters) == n]
        for words in anagram_words: words.sort()

    if not bingo:

        anagram_words=[words for letters, words in dict1.items() if len(words) > d]
        for words in anagram_words: words.sort()

    anagram_words_decorated=[(len(words),words) for words in anagram_words]
    anagram_words_decorated.sort(reverse=True)

    anagram_words_undecorated=[words for len_of_words, words in anagram_words_decorated]

    if print1:
        
        for words in anagram_words_undecorated:
            for word in words: print word,
            else: print
            
    return anagram_words_undecorated

        


    
    

