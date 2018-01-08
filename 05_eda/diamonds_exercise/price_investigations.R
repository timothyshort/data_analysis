library(ggplot2)
data(diamonds)

#Visualizations for Price
ggplot(aes(x=price), data=diamonds) +
  geom_histogram(binwidth = 500) +
  xlab('Price') + ylab('Count') +
  ggtitle('Price Distribution')

#Basic statistics
summary(diamonds$price)
mean(diamonds$price)
median(diamonds$price)

sum(diamonds$price < 500)
sum(diamonds$price < 250)
sum(diamonds$price >= 15000)

#Close look at price peak distribution
ggplot(aes(x=price), data=diamonds) +
  geom_histogram(binwidth = 25, color='gray') +
  scale_x_continuous(limits = c(250,1500), breaks=seq(250,1500,125)) +
  xlab('Price') + ylab('Count') +
  ggtitle('Price Distribution from $250 to $1,500')

ggsave('visualizations/PriceHistogram.png')
