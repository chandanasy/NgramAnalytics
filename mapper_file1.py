#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    l = line.strip().split()
    
    # create bigrams
    bigrams = [l[i:i+2] for i in range(len(l)-1)]
    
    for bigram in bigrams:
        
        # output goes to STDOUT (stream data that the program writes)
        print("{}\t{}".format(" ".join(bigram), 1))

