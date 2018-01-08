library(ggplot2)
load(diamonds)

#Investigate carats
by(diamonds$carat, diamonds$cut, summary)

#Price per carat by cut
ggplot(aes(x=price/carat), data=diamonds) +
  geom_histogram() +
  facet_wrap(~cut, scale="free") +
  scale_x_log10() +
  xlab('Price per Carat') + ylab('Cut') +
  ggtitle('Price per Carat by Cut')

ggsave('visualizations/PricePerCarat-CutImproved.png')
