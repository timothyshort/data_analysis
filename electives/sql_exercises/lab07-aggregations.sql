#SECTION 7 | SUMS

#Find the total amount of poster_qty paper ordered in the orders table.
SELECT sum(poster_qty)
FROM orders

#Find the total amount of standard_qty paper ordered in the orders table.
SELECT sum(standard_qty)
FROM orders

#Find the total dollar amount of sales using the total_amt_usd in the orders table.
SELECT sum(total_amt_usd)
FROM orders

#Find the total amount spent on standard_amt_usd and gloss_amt_usd paper for each order in the orders table. This should give a dollar amount for each order in the table.
SELECT (standard_amt_usd + gloss_amt_usd) as total
FROM orders

#Though the price/standard_qty paper varies from one order to the next. I would like this ratio across all of the sales made in the orders table.
SELECT sum(standard_amt_usd) / sum(standard_qty) AS standard_unit
FROM orders;


#SECTION 11 | MINS, MINS, AVG

#When was the earliest order ever placed?
SELECT min(occurred_at)
FROM orders

#Try performing the same query as in question 1 without using an aggregation function. 
SELECT occurred_at
FROM orders
ORDER BY occurred_at

#When did the most recent (latest) web_event occur?
SELECT max(occurred_at)
FROM web_events

#Try to perform the result of the previous query without using an aggregation function.
SELECT occurred_at
FROM web_events
ORDER BY occurred_at DESC
LIMIT 1

#Find the mean (AVERAGE) amount spent per order on each paper type, as well as the mean amount of each paper type purchased per order. Your final answer should have 6 values - one for each paper type for the average number of sales, as well as the average amount.
SELECT avg(standard_amt_usd) as avg_standard_cost,
	avg(standard_qty) as avg_standard_qty,
	avg(gloss_amt_usd) as avg_gloss_cost,
   	avg(gloss_qty) as avg_gloss_qty,
	avg(poster_amt_usd) as avg_poster_cost,
   	avg(poster_qty) as avg_poster_qty
FROM orders


# SECTION 14 | GROUP BY

#Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order.
SELECT min(orders.occurred_at), accounts.name
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY accounts.name
LIMIT 1

#Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name.
SELECT a.name as company, sum(o.total_amt_usd) as total_order_cost
FROM orders AS o
JOIN accounts a
ON a.id = o.account_id
GROUP BY a.name
ORDER BY a.name

#Via what channel did the most recent (latest) web_event occur, which account was associated with this web_event? Your query should return only three values - the date, channel, and account name.
SELECT we.occurred_at as date, we.channel as channel, a.name as name
FROM web_events we
JOIN accounts a
ON we.account_id = a.id
ORDER BY date DESC
LIMIT 1

#Find the total number of times each type of channel from the web_events was used. Your final table should have two columns - the channel and the number of times the channel was used.
SELECT channel, count(*)
FROM web_events
GROUP BY channel

#Who was the primary contact associated with the earliest web_event?
SELECT a.primary_poc, we.occurred_at
FROM web_events we
JOIN accounts a
ON we.account_id = a.id
ORDER BY we.occurred_at
LIMIT 1

#What was the smallest order placed by each account in terms of total usd. Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.
SELECT a.name as company, min(o.total_amt_usd) as smallest_order_usd
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY a.name
ORDER BY smallest_order_usd

#Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from fewest reps to most reps.
SELECT r.name as region, count(s.name) as sales_reps
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
GROUP BY region
ORDER BY sales_reps

#SECTION 16 | GROUP BY

#For each account, determine the average amount of each type of paper they purchased across their orders. Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account. 
SELECT a.name as company, avg(o.standard_qty) as avg_standard, avg(gloss_qty) as avg_gloss, avg(poster_qty) as avg_poster
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY company

#For each account, determine the average amount spent per order on each paper type. Your result should have four columns - one for the account name and one for the average amount spent on each paper type.
SELECT a.name as company, avg(o.standard_amt_usd) as avg_standard_cost, avg(gloss_amt_usd) as avg_gloss_cost, avg(poster_amt_usd) as avg_poster_cost
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY company

#Determine the number of times a particular channel was used in the web_events table for each sales rep. Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
SELECT s.name as sales_rep, we.channel as channel, count(*) as occurrences
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN web_events we
ON we.account_id = a.id
GROUP BY sales_rep, channel
ORDER BY occurrences DESC

#Determine the number of times a particular channel was used in the web_events table for each region. Your final table should have three columns - the region name, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
SELECT r.name, we.channel, count(*) as occurrences
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN web_events we
ON a.id = we.account_id
GROUP BY r.name, we.channel
ORDER BY occurrences DESC


#SECTION 20 | DISTINCT

#Use DISTINCT to test if there are any accounts associated with more than one region?
SELECT a.name as company, r.name as region
FROM accounts a
JOIN sales_reps s
ON a.sales_rep_id = s.id
JOIN region r
ON s.region_id = r.id

SELECT DISTINCT name
FROM accounts

#Have any sales reps worked on more than one account?
SELECT s.name as sales_rep, count(*) as num_accounts
FROM sales_reps s
JOIN accounts a
ON s.id = a.sales_rep_id
GROUP BY sales_rep
ORDER BY num_accounts

SELECT DISTINCT s.name as sales_rep
FROM sales_reps s


#SECTION 20 | HAVING

#How many of the sales reps have more than 5 accounts that they manage?
SELECT s.name as sales_rep, count(*) as num_accounts
FROM sales_reps s
JOIN accounts a
ON s.id = a.sales_rep_id
GROUP BY sales_rep
HAVING count(*) > 5

#How many accounts have more than 20 orders?
SELECT a.name as company, count(o.*) as orders
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY company
HAVING count(o.*) > 20

#Which account has the most orders?
SELECT a.name as company, count(o.*) as orders
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY company
ORDER BY orders DESC
LIMIT 1

#How many accounts spent more than 30,000 usd total across all orders?
SELECT a.name as company, sum(o.total_amt_usd) as total_spent
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY company
HAVING sum(o.total_amt_usd) > 30000
ORDER BY total_spent DESC

#How many accounts spent less than 1,000 usd total across all orders?
SELECT a.name as company, sum(o.total_amt_usd) as total_spent
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY company
HAVING sum(o.total_amt_usd) < 1000
ORDER BY total_spent

#Which account has spent the most with us?
SELECT a.name as company, sum(o.total_amt_usd) as total_spent
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY company
ORDER BY total_spent DESC
LIMIT 1

#Which account has spent the least with us?
SELECT a.name as company, sum(o.total_amt_usd) as total_spent
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY company
ORDER BY total_spent
LIMIT 1

#Which accounts used facebook as a channel to contact customers more than 6 times?
SELECT a.name as company, we.channel as channel, count(*) as contacts
FROM accounts a
JOIN web_events we
ON we.account_id = a.id
WHERE channel = 'facebook'
GROUP BY company, channel
HAVING count(*) > 6
ORDER BY contacts

#Which account used facebook most as a channel? 
SELECT a.name as company, we.channel as channel, count(*) as contacts
FROM accounts a
JOIN web_events we
ON we.account_id = a.id
WHERE channel = 'facebook'
GROUP BY company, channel
ORDER BY contacts DESC
LIMIT 1

#Which channel was most frequently used by most accounts?
SELECT a.name as company, we.channel as channel, count(*) as contacts
FROM accounts a
JOIN web_events we
ON we.account_id = a.id
GROUP BY company, channel
ORDER BY contacts DESC


#SECTION 27 | DATE

#Which year did Parch & Posey have the greatest sales in terms of total dollars? Are all years evenly represented by the dataset?
SELECT DATE_PART('year', occurred_at) as year, sum(total_amt_usd) as total_spent
FROM orders
GROUP BY DATE_PART('year', occurred_at)
ORDER BY total_spent DESC

#Which month did Parch & Posey have the greatest sales in terms of total dollars? Are all months evenly represented by the dataset?
SELECT DATE_TRUNC('month', occurred_at) as month, sum(total_amt_usd) as total_spent
FROM orders
GROUP BY DATE_TRUNC('month', occurred_at)
ORDER BY total_spent DESC
LIMIT 1

#Which year did Parch & Posey have the greatest sales in terms of total number of orders? Are all years evenly represented by the dataset?
SELECT DATE_PART('year', occurred_at) as month, sum(total) as total_orders
FROM orders
GROUP BY DATE_PART('year', occurred_at)
ORDER BY total DESC

#Which month did Parch & Posey have the greatest sales in terms of total number of orders? Are all months evenly represented by the dataset?
SELECT DATE_TRUNC('month', occurred_at) as month, sum(total) as total_orders
FROM orders
GROUP BY DATE_TRUNC('month', occurred_at)
ORDER BY total DESC
LIMIT 1

#In which month of which year did Walmart spend the most on gloss paper in terms of dollars?
SELECT a.name as company, DATE_TRUNC('month', o.occurred_at) as month, sum(o.gloss_amt_usd) as total_spent
FROM orders o
JOIN accounts a
ON a.id = o.account_id
WHERE a.name = 'Walmart'
GROUP BY DATE_TRUNC('month', o.occurred_at), a.name
ORDER BY total_spent DESC
LIMIT 1


#SECTION 31 | CASE

#We would like to understand 3 different branches of customers based on the amount associated with their purchases. The top branch includes anyone with a Lifetime Value (total sales of all orders) greater than 200,000 usd. The second branch is between 200,000 and 100,000 usd. The lowest branch is anyone under 100,000 usd. Provide a table that includes the level associated with each account. You should provide the account name, the total sales of all orders for the customer, and the level. Order with the top spending customers listed first.
SELECT a.name as company, sum(o.total_amt_usd) as total_sales,
	CASE WHEN sum(o.total_amt_usd) > 200000 THEN 'TOP'
    	WHEN sum(o.total_amt_usd) > 100000 THEN 'MID'
        ELSE 'LOW' END
        as level
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name
ORDER BY total_sales DESC

#We would now like to perform a similar calculation to the first, but we want to obtain the total amount spent by customers only in 2016 and 2017. Keep the same levels as in the previous question. Order with the top spending customers listed first.
SELECT a.name as company, sum(o.total_amt_usd) as total_sales,
	CASE WHEN sum(o.total_amt_usd) > 200000 THEN 'TOP'
    	WHEN sum(o.total_amt_usd) > 100000 THEN 'MID'
        ELSE 'LOW' END
        as level
FROM accounts a
JOIN orders o
ON a.id = o.account_id
WHERE o.occurred_at BETWEEN '2016-01-01' AND '2017-12-31'
GROUP BY a.name
ORDER BY total_sales DESC

#We would like to identify top performing sales reps, which are sales reps associated with more than 200 orders. Create a table with the sales rep name, the total number of orders, and a column with top or not depending on if they have more than 200 orders. Place the top sales people first in your final table.
SELECT s.name as sales_rep, count(o.*) as total_sales,
	CASE WHEN count(o.*) > 200 THEN 'TOP' END as level
FROM sales_reps s
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON o.account_id = a.id
GROUP BY s.name
ORDER BY total_sales DESC

#The previous didn't account for the middle, nor the dollar amount associated with the sales. Management decides they want to see these characteristics represented as well. We would like to identify top performing sales reps, which are sales reps associated with more than 200 orders or more than 750000 in total sales. The middle group as any rep with more than 150 orders or 500000 in sales. Create a table with the sales rep name, the total number of orders, total sales across all orders, and a column with top, middle, or low depending on this criteria. Place the top sales people based on dollar amount of sales first in your final table. You might see a few upset sales people by this criteria!
SELECT s.name as sales_rep, count(o.*) as total_sales, sum(o.total_amt_usd) as revenue,
	CASE WHEN count(o.*) > 200 OR sum(o.total_amt_usd) > 750000 THEN 'TOP'
    	WHEN count(o.*) > 150 OR sum(o.total_amt_usd) > 500000 THEN 'TOP'
        ELSE 'LOW'
    END as level
FROM sales_reps s
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON o.account_id = a.id
GROUP BY s.name
ORDER BY revenue DESC