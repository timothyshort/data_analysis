#3

SELECT DATE_TRUNC('day', occurred_at) as date, channel, count(*) as num_of_events
FROM web_events
GROUP BY date, channel

SELECT channel, avg(num_of_events)
FROM
    (SELECT DATE_TRUNC('day', occurred_at) as date, channel, count(*) as num_of_events
     FROM web_events
     GROUP BY date, channel) as subq
GROUP BY channel


#7 

SELECT DATE_TRUNC('month', min(occurred_at)) as first_order
FROM orders

SELECT DATE_TRUNC('month', occurred_at),
    avg(standard_qty) as avg_standard, avg(gloss_qty) as avg_gloss, avg(poster_qty) as avg_poster,
    sum(total_amt_usd) as total_spent
FROM orders
WHERE DATE_TRUNC('month', occurred_at) =
    (SELECT DATE_TRUNC('month', min(occurred_at)) as first_order
    FROM orders)
    GROUP BY DATE_TRUNC('month', occurred_at)
    
    
#9

#Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
SELECT t3.sales_reps, t3.region, t3.total_sales
FROM
    (SELECT s.name sales_reps, r.name as region, sum(o.total_amt_usd) as total_sales
    FROM region r
    JOIN sales_reps s
    ON r.id = s.region_id
    JOIN accounts a
    ON s.id = a.sales_rep_id
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY s.name, r.name) t3
JOIN
    (SELECT region_name, max(total_sales) as total_sales
    FROM
        (SELECT s.name sales_reps, r.name as region_name, sum(o.total_amt_usd) as total_sales
        FROM region r
        JOIN sales_reps s
        ON r.id = s.region_id
        JOIN accounts a
        ON s.id = a.sales_rep_id
        JOIN orders o
        ON a.id = o.account_id
        GROUP BY s.name, r.name) as t1
     GROUP BY region_name) as t2
ON t2.total_sales = t3.total_sales

#For the region with the largest sales total_amt_usd, how many total orders were placed? 
SELECT r.name as region_name, sum(o.total_amt_usd) as total_sales, sum(o.total) as total_orders
FROM orders o
JOIN accounts a
ON a.id = o.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id
GROUP BY region_name
ORDER BY total_sales DESC
LIMIT 1

#For the name of the account that purchased the most (in total of their lifetime as a customer) standard_qty paper, how many accounts still had more in total purchases? 
SELECT a.name as company, sum(o.standard_qty) as total_standard_sales, sum(o.total) as total_sales
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY company
HAVING sum(o.total) >
  (SELECT t1.total_sales
  FROM
  (SELECT a.name as company, sum(o.standard_qty) as total_standard_sales, sum(o.total) as total_sales
  FROM orders o
  JOIN accounts a
  ON o.account_id = a.id
  GROUP BY company
  ORDER BY total_standard_sales DESC
  LIMIT 1) as t1)

#For the customer that spent the most (in total of their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?
SELECT we.channel as channel, count(*) as events
FROM orders o
JOIN accounts a
ON o.account_id = a.id
JOIN web_events we
ON a.id = we.account_id
AND a.name =
  (SELECT company FROM
    (SELECT a.name as company
    FROM orders o
    JOIN accounts a
    ON o.account_id = a.id
    GROUP BY company
    ORDER BY company DESC
    LIMIT 1)
   as t1)
GROUP BY we.channel
ORDER BY events DESC

#What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?
SELECT company, avg(total_sales)
FROM
    (SELECT a.name as company, sum(o.total_amt_usd) as total_sales
    FROM orders o
    JOIN accounts a
    ON o.account_id = a.id
    GROUP BY company
    ORDER BY total_sales DESC
    LIMIT 10)
    as t1
GROUP BY company

#What is the lifetime average amount spent in terms of total_amt_usd for only the companies that spent more than the average of all orders.
SELECT a.name as company, avg(o.total_amt_usd) as avg_total_sales
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY company
HAVING avg(o.total_amt_usd) >
    (SELECT avg(avg_total_sales)
    FROM
        (SELECT a.name as company, avg(o.total_amt_usd) as avg_total_sales
        FROM orders o
        JOIN accounts a
        ON o.account_id = a.id
        GROUP BY company)
        as t1)
ORDER BY avg_total_sales

#13

WITH t3 AS (
    SELECT s.name sales_reps, r.name as region_name, sum(o.total_amt_usd) as total_sales
    FROM region r
    JOIN sales_reps s
    ON r.id = s.region_id
    JOIN accounts a
    ON s.id = a.sales_rep_id
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY s.name, r.name
    ),
    
    t2 AS (
    SELECT region_name, max(total_sales) as total_sales
    FROM t3
    GROUP BY region_name)    

SELECT t3.sales_reps, t3.region_name, t3.total_sales
FROM t3
JOIN t2
ON t2.total_sales = t3.total_sales