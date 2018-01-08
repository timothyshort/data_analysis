library(ggplot2)
data(diamonds)

by(diamonds$price, diamonds$cut, summary)

#Visualizations for Price by Cut
ggplot(aes(x=price), data=diamonds) +
  geom_histogram() +
  facet_wrap(~cut)

(by(diamonds$price, diamonds$cut, max))
(by(diamonds$price, diamonds$cut, min))
(by(diamonds$price, diamonds$cut, median))

?facet_wrap

ggplot(aes(x=price), data=diamonds) +
  geom_histogram() +
  facet_wrap(~cut, scales="free") + 
  ggtitle('Price per Carat Distributions by Cut')
ggsave('visualizations/PricePerCarat-byCut.png')
