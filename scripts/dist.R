#!/usr/bin/env Rscript

# leave the silly outlier out for better plots

blocktimes = as.matrix(read.csv(file = "../data/diffs.csv", head = FALSE))
blocktimes = setNames(blocktimes, c("blocktime"))
summary(blocktimes)
quantile(blocktimes, c(0.9, 0.95, 0.99, 0.999, 0.9999))
png(file = "blocktimedistro.png",width = 1000,height = 350)
hist(blocktimes, breaks = 600, freq = FALSE)
dev.off()
