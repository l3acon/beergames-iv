#!/usr/bin/env python

import random
import sys

for i in range(int(sys.argv[1])):
    print random.randint(1,0x7FFFFFFF)

