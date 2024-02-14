#!/usr/bin/python

import sys

current_trigram = None
current_sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    trigram, count = line.strip().split("\t", 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if trigram == current_trigram:
        current_sum += count
    else:
        if current_trigram:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%d" %( current_trigram, current_sum ))
        current_trigram = trigram
        current_sum = count

# output count for the last trigram
if current_trigram:
    # output goes to STDOUT (stream data that the program writes)
    print("%s\t%d" %( current_trigram, current_sum ))
