# Chapter 11 Section 2 Exercise 3

def file_dict(filename= 'words.txt'):
    """ Exercise 1 """
    fin = open(filename)
    dict_ = dict()
    for word in fin:
        dict_[word.strip()] = 1
    fin.close()
    return dict_

def histogram(s): 
    """ Exercise 2 """
    d = dict() 
    for c in s: 
        d[c] = d.get(c,0) + 1
    return d

def print_hist(h):
    """ Exercise 3 """
    lis = []
    for c in h:
        lis.append([c,h[c]])
    lis.sort()
    for c in lis:
        print c, lis[c], '\n'

if __name__ == '__main__':

    dict_ = file_dict(*sys.argv)
    hist = histogram(dict_)
    print_hist(hist)


        







        
        

