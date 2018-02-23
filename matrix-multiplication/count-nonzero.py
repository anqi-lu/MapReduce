# Author: Anqi Lu
# Feb 21, 2018
# Big Data Management Spring 2018

"""Count non-zero rows and columns after matrix multiplication"""

with open('out.txt', 'r') as f:
  data = f.readlines()

# split into matrix
import numpy as np
K = 10000
mtx = np.zeros((K, K))

for row in data:
  loc, val = row.strip().split('\t')
  i, j = loc.split(' ')
  i, j = int(i), int(j)
  val = float(val)
  mtx[i,j] = val

rows = np.sum(mtx, axis=1)
cols = np.sum(mtx, axis=0)

rows_val = np.sum(rows != 0)
cols_val = np.sum(cols != 0)

print rows_val
print cols_val