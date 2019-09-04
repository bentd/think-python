import os

def walker1(dir_):
    walK=os.walk(dir_)
    for items in walK:
        print '\n',items[0]
        for item in items[1]: print item
        for item in items[2]: print item

def walker2(dir_):
    walK=os.walk(dir_)
    for items in walK:
        for item in items[2]:
            print os.path.join(items[0],item)
            
walker1(os.getcwd())
walker2(os.getcwd())
    
