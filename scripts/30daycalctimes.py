import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

with open('../data/30dayblocktimes.csv', 'rb') as f:
    a = np.loadtxt(f, dtype='int64')

diffs = np.diff(a)
i = np.where(diffs == 13013)
diffs = np.delete(diffs, i)
y = np.bincount(diffs)
ii = np.nonzero(y)[0]

data = zip(ii, y[ii])
with open('../data/30daydiffs.csv', 'wb') as f:
    writer = csv.writer(f)
    for word in diffs:
            writer.writerow([word])
