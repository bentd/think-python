# Chapter 10 Section 8 Exercise 5

def chop(t):
    if len(t) in [0,1,2]: 
	t = []
    else: 
	t.pop(0)
	t.pop(-1)
    return None

if __name__ == '__main__':

	list1 = ['a', 5, 6, 'h', 007, 'koi']
	chop(list1)
	print list1










        

        
