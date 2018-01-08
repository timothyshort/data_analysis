library(ggplot2)
data(diamonds)

by(diamonds$price, diamonds$color, summary)
by(diamonds$price, diamonds$color, summary)['D']
by(diamonds$price, diamonds$color, summary)['J']

IQR(subset(diamonds,color=="D")$price)
IQR(subset(diamonds,color=="J")$price)