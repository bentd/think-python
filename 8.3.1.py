# Chapter 8 Section 3 Exercise 1 (Traversals)

def backward(apple):
    """ Takes a string and prints each letter individualy

        An example of traversals with """
    index = -1
    while index > -(len(apple))-1:
        letter = apple[index]
        print letter
        index += -1
    return

def run(name, string):
    backward(string)

if __name__ == '__main__':

    run()
