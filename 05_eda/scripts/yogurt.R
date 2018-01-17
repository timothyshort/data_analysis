library(ggplot2)
yo = read.csv('datasets/yogurt.csv')

yo$id = factor(yo$id)
str(yo)

#Histogram of prices
ggplot(aes(x=price), data=yo) + geom_histogram() + ggtitle('Distribution of Costs of Yogurt')

#Histogram of all purchases
yo$all_purchases = yo$strawberry + yo$blueberry + yo$pina.colada + yo$plain + yo$mixed.berry
ggplot(aes(x=all_purchases), data=yo) + geom_histogram()

#Scatter plot
ggplot(aes(x=time, y=price), data=yo) + geom_jitter(alpha=.1)

#Look at samples of households
set.seed(55)
sample.ids = sample(levels(yo$id), 16)
sample.ids
ggplot(aes(x=time, y=price), data=subset(yo, id %in% sample.ids)) +
  facet_wrap(~id) + geom_line() + geom_point(aes(size=all_purchases), pch=1)
