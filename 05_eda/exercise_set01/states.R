statesInfo <- read.csv('datasets/stateData.csv')
subset(statesInfo, state.region == 1)

#consider state region subsets
region2States = statesInfo[statesInfo$state.region == 2,]
head(region2States)

region1Subset = subset(statesInfo, state.region == 1 , )
head(region1Subset)