#!/usr/bin/env python

"""Mapper for word count"""
import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    # split the line into words
    for word in pattern.findall(line):    
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word.lower(), 1)

