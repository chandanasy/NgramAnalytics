#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    l = line.strip().split()
    
    # Generate trigrams from the words in the input line
    for i in range(len(l)-2):
        trigram = l[i:i+3]
        # output goes to STDOUT (stream data that the program writes)
        print("%s\t%d" %(' '.join(trigram), 1))
