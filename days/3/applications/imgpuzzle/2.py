#!/usr/bin/python

def eliminate_duplicates_and_print_sorted(file):
	for line in sorted(set(file)):
		print line
    #remove duplicate lines from `file' and print the sorted lines
    #hint: you can use a set and also the "sorted" function

if __name__ == '__main__':
    eliminate_duplicates_and_print_sorted(open('2.txt'))
    
