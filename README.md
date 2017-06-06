# ethblocks

Playing with eth blocktimes
- To collect the blocktimes (works on --fast synced nodes or full nodes, but I
  couldn't get it to work at all with --light as you need a server full node to
  be willing to fetch you all the data), run: `geth --exec
  'loadScript("./blocktime/collectBlockTimes.js")' attach > blocktimes.csv`
- At [block 116521](https://etherscan.io/block/116521), there was a consensus
  issue meaning the next block was mined [13013 seconds
  later](https://etherscan.io/block/116522).  I've left this out of the plots
  because I was feeling sassy.
