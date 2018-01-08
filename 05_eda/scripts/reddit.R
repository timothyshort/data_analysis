redditData = read.csv('datasets/reddit.csv')

table(redditData$employment.status)

str(redditData)
summary(redditData)

library(ggplot2)
qplot(data=redditData, x=age.range)

#order the age range
levels(redditData$age.range)
redditData$age.range <- ordered(redditData$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above", "NA"))
qplot(data = redditData, x=age.range)

#order income level
levels(redditData$income.range)
redditData$income.range = ordered(redditData$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999", "$40,000 - $49,999", "$50,000 - $69,999",
"$70,000 - $99,999", "100,000 - $149,999", "$150,000 or more"))
qplot(data=redditData, x=income.range)