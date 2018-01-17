library(ggplot2)
library(reshape2)

#Read gene expression dataset
nci = read.table('datasets/nci.tsv')
colnames(nci) = c(1:64)
head(nci)
names(nci)

#Reshape to long format
nci.long.samp = melt(as.matrix(nci[1:500, ]))
names(nci.long.samp) = c('gene', 'case', 'value')
head(nci.long.samp)

#Heat map
ggplot(aes(x=case, y=gene, fill=value), data=nci.long.samp) +
  geom_tile() +
  scale_fill_gradientn(colors=colorRampPalette(c('blue', 'red'))(100)) +
  ggtitle('Heat Map for Detecting Cases in Genes')
