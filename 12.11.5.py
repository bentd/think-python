from anagram import anagrams


def metathesis(anagram=anagrams(print1=False)):
    
    for words in anagram:

        for word1 in words:

            for word2 in words:

                count=0

                for letter1,letter2 in zip(word1,word2):
                    if letter1 != letter2: count+=1

                if count == 2:
                    print word1, word2
    
metathesis()
