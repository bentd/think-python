# Chapter 10 Section 15 Exercise 11

# NEED TO FIX

from bisect import bisect_right
import sys

def read_file(filename= 'words.txt'):
    t = []
    fin = open(filename)
    re = fin.read()
    fin.close()
    return re.split('\n')
    
def bisect_1(lis, string):
    
    """ This bisect search works by creating an index list of the
            indices of the list 'lis' provided
            
        The middle item of the index list is
            used as an index to call out a lis item
            
        If that lis item is the string provided then that index
            item is returned
            
        Otherwise the index list is shortened to the possible indices
            within the list (lis) provided that could contain the string

        EXAMPLE

        string provided

        'A'
        

        lis provided

        | 'A' | 'E' | 'L' | 'P' | 'P' |
        |     |     |     |     |     |
        |  0  |  1  |  2  |  3  |  4  |
        

        the index list (sort of like a index magnifying glass)

        |  0  |  1  |  2  |  3  |  4  |
      
        is middle item in the index list (value: 2) the index of the
            item (value: 'L' index: 2) in  lis which carries the
            same value as the string provided ? NO
        is 'A' lower or greater than that item? lower!


        next index list

        |  0  |   1  |

        is the middle item in the index list (value: 1) the index of lis
             item (value: 'E' index: 1) that carries the same value of
             the string provided? NO
        is 'A' lower or greater than that item? lower!


        next index list

        |  0  |

        is the middle index list item (value: 0) the index of the lis
            item that carries the value of the string provided? YES
        0 (type - 'int') is returned

        """
    
    s = range(len(lis))
    
    while len(s) > 0:
        
        middle_s_item = s[len(s) / 2]
        
        if lis[middle_s_item] == string: return s[middle_s_item]
        
        elif lis[middle_s_item] > string: s = s[ : len(s) / 2]
        
        elif lis[middle_s_item] < string: s = s[len(s) / 2 + 1 : ]
    
    return -1

def bisect_2(lis, word):
    " I commandeered Authors idea of using built-in function bisect_left "
    
    bis = bisect_right(lis, word)
    if (bis < len(lis)) and (lis[bis] == word): return bis-1

def main(name, filename= 'words.txt', string='zzuba', *args):

    read = read_file(filename)
    print len(read)

    b1 = bisect_1(read, string)
    b2 = bisect_2(read, string)

#   print string, bl, read[bl]
    print string, b1, read[b1]
    print string, b2, read[b2]

if __name__ == '__main__':

    main(*sys.argv)










        

        
