# Chapter 9 Section 1 Exercise 1

# Reads a file and prints any lines that are longer than a given length

def longer(filename, length = 20):
    """ Finds and prints lines within a file that are greater
        in length than the default integer 'length' """
    fin = open(filename)   
    for line in fin:
        line = line.strip
        if len(line) > length: print line
        else: continue

def run(name, filename = 'words.txt', length = 20):

    longer(filename, length)


if __name__ == '__main__':

    run()
