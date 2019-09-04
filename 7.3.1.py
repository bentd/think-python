# Think Python Chapter 7 Section 3 Exercise 1

import sys

def print_n(string, n):

	for x in range(n): print string

def main(name, string= 'Hello, World!', n= 5):

	n = int(n)
	
	print_n(string, n)

if __name__ == '__main__':

	main(*sys.argv)

