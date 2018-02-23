#!/usr/bin/env python
import sys
I = 2
K = 2
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    name, i, j, val = line.split()
    if name == 'M':
      for k in range(K):
        print '%s %s\t%s %s %s' % (i, k, name, j, val)
    else:
      j, k = i, j
      for i in range(I):
        print '%s %s\t%s %s %s' % (i, k, name, j, val)
