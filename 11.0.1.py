# Chapter 11 Exercise 1

import sys

def file_dict(filename= 'words.txt'):
    """ Exercise 1 """
    fin = open(filename)
    dict_ = dict()
    for word in fin:
        dict_[word.strip()] = 1
    fin.close()
    return dict_


if __name__ == '__main__':

    print file_dict(*sys.argv)






        
        

