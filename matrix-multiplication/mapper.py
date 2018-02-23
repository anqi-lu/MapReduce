#!/usr/bin/env python

# Author: Anqi Lu
# Feb 21, 2018
# Big Data Management Spring 2018
# Algorithm taken from Book [Mining of Massive Datasets] by Leskovec, Rajaraman and Ullman

"""Mapper function for matrix multiplication"""

import sys

K_M = 10000
K_N = 10000

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for line in data:
        # Reduce step, i.e. the input for reducer.py
        name, i, j, val = line
        
        if name == 'M':
            for k in range(K_M):
                print("{} {}\t{} {} {}".format(i, k, name, j, val)) 
        if name == 'N':
            for k in range(K_N):
                print("{} {}\t{} {} {}".format(k, j, name, i, val))

if __name__ == "__main__":
    main()

