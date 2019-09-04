# Chapter 10 Section 8  Exercise 4

def middle(t):

    if len(t) in [0,1,2]: return []
    return t[1 : len(t)- 1]

if __name__ == '__main__':

	list1 = [1, 2, 3, 4]
	list2 = middle(list1)
	print list1
	print list2

