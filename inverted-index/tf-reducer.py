#! /usr/bin/python
 
# Author: Anqi Lu
# Feb 22, 2018
# Big Data Management Spring 2018
# Algorithm taken from Book [Data-intensive Text Processing with MapReduce] by  Lin & Dyer 

"""Reducer function for building inverted index"""

from sys import stdin
import re
 
prev_t = None
P = []

for line in stdin:
    line = line.strip()
    t, id, tf = line.split()

    if t != prev_t and prev_t is not None:
        print("{}\t{}".format(prev_t, P))
        P = []
    P.append((id, tf))
    prev_t = t

print("{}\t{}".format(t, P))