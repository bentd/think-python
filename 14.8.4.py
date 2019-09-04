from os import walk,popen,getcwd

from os.path import join

def ext_test(path, ext):
    
    " Tests whether a file has given extension via the last characters in the file name "
    
    len1=len(path)
    len2=len(ext)
    
    if len2 > len1: return False
    elif path[len1-len2:] == ext: return True    
    else: return False

def chksum(path):
    
    " Returns a path's md5 checksum "
    
    fp=popen('md5sum %s' %path)
    res=fp.read()
    fp.close
    index=res.find(' ')
    
    return res[:index]
    
def ext_list(directory, ext):
    
    " Returns a list of all files within the given directory that have the given file extension "
    
    walks=walk(directory)
    lis=[]
    
    for path,folders,files in walks:
        lis.extend([join(path,fil) for fil in files if ext_test(fil,ext)])
        
    return sorted(lis)

def chksumdic(lis):
    
    " Creates a dictionary that maps each path to that particular file's checksum "
    
    dic={}
    for path in lis:
        dic[chksum(path)]=dic.get(chksum(path),[])+[path]
        
    return dic

def print_duplicates(dic):
    
    " Prints files that are duplicates of each other "
    
    lis=[lis for chksum,lis in sorted(dic.items()) if len(lis)>1]
    for files in lis:
        for fil in files: print fil,
        else: print
  

if __name__ == '__main__':

    cwd=getcwd()
    
    files=ext_list(cwd,'.py')
    
    dictionary=chksumdic(files)
    
    print_duplicates(dictionary)
