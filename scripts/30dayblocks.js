
// geth --exec 'loadScript("./collectmissingblocks.js")' attach > 30dayblocktimes.csv

var times =[];
var fromblock = eth.blockNumber - 162000;
// 2592000 seconds in 30 days
// which means approx 162000 blocks (assuming mean blocktime = 16 seconds)

for (i = fromblock; i < eth.blockNumber; i++) {
  var blk = web3.eth.getBlock(i)
  console.log(blk.timestamp);
}
