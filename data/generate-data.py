#!/usr/bin/env python

import random
import sys
import math
import copy

usage="""
./generate-data.py <size>
    <size> should be significantly smaller than the max integer value, assumed 
    to be the largest non-negative 32-bit integer.
"""

if len(sys.argv) < 1:
    print(usage)
    sys.exit()

size=int(sys.argv[1])   # size of output
min_value=1
max_value=0x7FFFFFFF    # largest 32-bit value
sparsity=4              # ratio of unique numbers to duplicated numbers

"""
Generate non repeating list of random numbers. This is slow and an infinite 
loop if size > max_value.
"""
s=set()
while len(s) < math.floor(size/sparsity/2): # assume this is reasonable
    s.add(random.randint(min_value, max_value))

"""
Choose the special numbers.
"""
odd_value=random.choice(list(s))
odd_index=random.randint(0, len(s)-1)

#print "odd_value: "+str(odd_value)

"""
Make a list of sets.
"""
data=list()
for i in range(0, sparsity*2):
    data.append(copy.copy(s))

"""
Barf it out whilst keeping some track of things. Not exactly random but not 
really predictable either.
"""
counter=0
while len(data) > 0:
    current_set=random.choice(data)
    if(len(current_set) == 0):
        data.remove(current_set)
    else:
        print(current_set.pop())
        counter=counter+1
        if counter == odd_index:
            print odd_value
    
