import csv
import numpy as np

with open('unixtime.csv', 'rb') as f:
    a = np.loadtxt(f, dtype='int64')
diffs = np.diff(a)
i = np.where(diffs == 13013)
diffs = np.delete(diffs, i)
y = np.bincount(diffs)
ii = np.nonzero(y)[0]
print zip(ii, y[ii])
