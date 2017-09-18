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

#5. Import data into RStudio
    #Add library(ggplot)
ggplot(global_temp_data, aes(x=year)) + geom_point(aes(y=avg_temp), size=.5, color="gray") + geom_line(aes(y=moving_avg_14), color="blue", size=1)

ggplot(columbus_temp_data, aes(x=year)) + geom_point(aes(y=avg_temp), size=.5, color="gray") + geom_line(aes(y=moving_avg_14), color="red", size=1)