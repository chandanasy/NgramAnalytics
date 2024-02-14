#!/usr/bin/python

import sys

current_bigram = None
current_sum = 0

# input comes from STDIN
for line in sys.stdin:
    
    bigram, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if bigram == current_bigram:
        current_sum += count
    else:
        if current_bigram:
            # output goes to STDOUT (stream data that the program writes)
            print("{}\t{}".format(current_bigram, current_sum))
        current_bigram = bigram
        current_sum = count

# output the last bigram
if current_bigram:
    print("{}\t{}".format(current_bigram, current_sum))