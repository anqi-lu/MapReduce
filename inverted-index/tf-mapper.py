#! /usr/bin/python
 
# Author: Anqi Lu
# Feb 22, 2018
# Big Data Management Spring 2018
# Algorithm taken from Book [Data-intensive Text Processing with MapReduce] by  Lin & Dyer 

"""Mapper function for building inverted index"""

import sys
import re
import glob


def mapper(id, content):
    H = {}
    # words = re.findall(r'\w+', content)
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")

    for word in pattern.findall(content):
        H[word.lower()] = H.get(word.lower(), 0) + 1
    for k, v in H.iteritems():
        
        print("{} {}\t{}".format(k, id, v))
  
       

if __name__ == "__main__":
    base_path = 'docs/'
    files = glob.glob(base_path + '*.txt')
    for i, file_name in enumerate(files):
        with open(file_name, 'r') as f:
            read_data = f.read()
            mapper(i, read_data)