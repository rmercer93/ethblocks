# ethblocks

Playing with eth blocktimes
- To collect the blocktimes (works on --fast synced nodes or full nodes, but I
  couldn't get it to work at all with --light as you need a server full node to
  be willing to fetch you all the data), run: `geth --exec
  'loadScript("./blocktime/collectBlockTimes.js")' attach > blocktimes.csv`
- At [block 116521](https://etherscan.io/block/116521), there was a consensus
  issue meaning the next block was mined [13013 seconds
  later](https://etherscan.io/block/116522).  I've left this out of the plots.


```
  Min.    1st Qu.   Median    Mean    3rd Qu.   Max.
  1.00    5.00      11.00     15.29   21.00     13010.00

  90%   95%   99%
  34    44    67

// Without the silly outlier, we have this:
  Min.    1st Qu.   Median    Mean    3rd Qu.   Max.
  1.00    5.00      11.00     15.29   21.00     300.00

```


