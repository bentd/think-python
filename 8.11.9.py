# Chapter 8 Section 11 Exercise 9

def is_reverse(word1, word2):

    len1 = len(word1)
    len2 = len(word2)
    
    if len1 != len2: return False
    
    i = 0
    j= -1
    
    while j >= -len2:
        if word1[i] != word2[j]: return False
        i += 1
        j -= 1

    return True


if __name__ == '__main__':

    print is_reverse('star','rats')
