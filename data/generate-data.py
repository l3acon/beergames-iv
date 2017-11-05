#!/usr/bin/env python

import random
import sys
import math

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
while len(s) < math.floor(size/sparsity/2):
    s.add(random.randint(min_value, max_value))

odd_value=s.pop()

"""
Dump out elements 
"""
print(str(odd_value))
for run in range(1,int(sparsity)*2):
    for i in s:
        print(str(i))
    print(str(odd_value))
