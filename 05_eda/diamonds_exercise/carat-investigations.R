library(ggplot2)
data(diamonds)


ggplot(aes(x=carat), data=diamonds) +
  geom_freqpoly()


ggplot(aes(x=carat), data=diamonds) +
  geom_freqpoly(binwidth=.01) +
  scale_x_continuous(breaks = seq(0,5,.2)) +
  ggtitle('Distribution of Carats')
ggsave('visualizations/DistributionCarats.png')
