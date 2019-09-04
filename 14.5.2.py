

def sed(pattern,replacement,file1,file2):
    
    try:
        file1=open('file1.txt','r')
        file2=open('file2.txt','w')

        for line in file1:
            if pattern in line: file2.write(line.replace(pattern,replacement))
            else: file2.write(line)

        file1.close()
        file2.close()
        
    except IOError:
        print 'Sorry! No such file or directory...\nPlease try again.'
  


    
    
        
