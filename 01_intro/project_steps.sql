#1. Find available cities in the United States using the city_list table
SELECT *
FROM city_list
WHERE country = 'United States'

#2. Once I find the city near me, look up the data from the city_data table
SELECT *
FROM city_data
WHERE city = 'Columbus'

    #Download the results as a CSV with only the year and avg_temp columns
    SELECT year, avg_temp
    FROM city_data
    WHERE city = 'Columbus'

#3. Look up the global_data table; download CSV
SELECT *
FROM global_data

#4. Add 7-day and 14-day moving averages in Excel, export to CSV
average(B2:B8)
average(B2:B15)


#5. Import data into RStudio
    #Add library(ggplot)
    
ggplot(columbus_temp_data, aes(x=year)) + ylim(12,16) + geom_line(aes(y=moving_avg_14), color="red", size=1) + geom_point(aes(y=avg_temp), size=.5, color="gray")

ggplot(global_temp_data, aes(x=year)) + ylim(6,10) + geom_line(aes(y=moving_avg_14), color="blue", size=1) + geom_point(aes(y=avg_temp), size=.5, color="gray")

#6. Analyze

#Compare City vs Global temperatures by looking at the average and the most recent 14-year moving average
global_avg = median(global_temp_data$avg_temp[global_temp_data$year>1750], na.rm = TRUE)
> 8.37 
columbus_avg = median(columbus_temp_data$avg_temp[columbus_temp_data$year>1750], na.rm = TRUE)
> 14.06

tail(global_temp_data$moving_avg_14,1)
> 9.58
tail(columbus_temp_data$moving_avg_14,1)
> 15.03

#Find the average change from year 1763 to 2013
(global_temp_data$moving_avg_14[264] - global_temp_data$moving_avg_14[14]) / (264-14)
> .00596
(columbus_temp_data$moving_avg_14[271] - columbus_temp_data$moving_avg_14[21]) / (271-21)
> .0074