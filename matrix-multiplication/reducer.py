#!/usr/bin/env python

# Author: Anqi Lu
# Feb 21, 2018
# Big Data Management Spring 2018
# Algorithm taken from Book [Mining of Massive Datasets] by Leskovec, Rajaraman and Ullman

"""Reducer function for matrix multiplication"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def split(item):
    return item.split(' ')

def item_name(item):
    return item[0]

def item_idx(item):
    return item[1]

def item_val(item):
    return float(item[2])

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, lambda x:x[0]):
        lines = [split(item) for _, item in group]
        m = [item for item in lines if item_name(item) is 'M']
        n = [item for item in lines if item_name(item) is 'N']        
        running_sum = 0
        n_idx = 0

        for m_idx in range(len(m)):
        
            if len(n) == 0:
                break

            m_idx_val = item_idx(m[m_idx])
            m_val = item_val(m[m_idx])
            n_idx_val = item_idx(n[n_idx])

            while n_idx_val < m_idx_val and n_idx < len(n) - 1:
                n_idx += 1
                n_idx_val = item_idx(n[n_idx])

            if n_idx_val > m_idx_val:
                continue
            
            if n_idx_val == m_idx_val:
                running_sum += m_val * item_val(n[n_idx])

        print("{}\t{}".format(current_word, str(running_sum)))

if __name__ == "__main__":
    main()

