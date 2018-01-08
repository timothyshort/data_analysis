library(ggplot2)
data(diamonds)

#Boxplots of price by categoricals cut, clarity, color

ggplot(aes(x=cut, y=price), data=diamonds) +
  geom_boxplot()+ ggtitle('Price by Cut') 
ggsave('visualizations/Boxplot-CutPrice.png')

ggplot(aes(x=clarity, y=price), data=diamonds) +
  geom_boxplot()+ ggtitle('Price by Clarity') 
ggsave('visualizations/Boxplot-ClarityPrice.png')

ggplot(aes(x=color, y=price), data=diamonds) +
  geom_boxplot()+ ggtitle('Price by Color') 
ggsave('visualizations/Boxplot-ColorPrice.png')

ggplot(aes(x=color, y=price/carat), data=diamonds) +
  geom_boxplot()+ ggtitle('Price per Carat by Color') 
ggsave('visualizations/Boxplot-PriceCarat-byColor.png')
