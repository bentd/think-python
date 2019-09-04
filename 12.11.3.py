

fin=open('textsample.txt','r')
string_arg=''

for line in fin:
    line=line.strip().lower()+' '
    string_arg+=line


def histogram2(s): 
    """ Exercise 2 """
    d = dict() 
    for c in s: 
        d[c]=d.get(c,0)+1
    return d

def invert_dict2(d):
    """ Excercise """
    inverse=dict()
    for key in d:
        if inverse.get(d[key]) is None:inverse[d[key]]=[inverse.setdefault(d[key],key)]
        else: inverse[d[key]].append(key)
    return inverse

frequency1=histogram2(string_arg)
frequency2=invert_dict2(frequency1)
frequency3=frequency2.items()
frequency3.sort()

for key, value in frequency3:
    for letter in value:
        print key, letter
    print '\n'






