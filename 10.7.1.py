# Chapter 10 Section 7 Exercise 1

def nested_sum(a):

    total = 0

    for element in a:
        if isinstance(element, list): total += nested_sum(element)
	eif isinstance(element, int): total += element
	eif isinstance(element, float): total += element
        else: continue

    return total


if __name__ == '__main__':

	print nested_sum([[1,2],[3,4],'a',[5,6],'b']

