#SECTION 4

SELECT orders.*, accounts.*
FROM accounts
JOIN orders
ON accounts.id = orders.account_id;

SELECT accounts.website, accounts.primary_poc,
	orders.standard_qty, orders.gloss_qty, orders.poster_qty
FROM accounts
JOIN orders
ON accounts.id = orders.account_id;


#SECTION 11

SELECT accounts.primary_poc, web_events.occurred_at, web_events.channel
FROM web_events
JOIN accounts
ON web_events.account_id = accounts.id
WHERE accounts.name = 'Walmart';

SELECT region.name region, sales_reps.name rep, accounts.name account
FROM sales_reps
JOIN region
ON region.id = sales_reps.region_id
JOIN accounts
ON sales_reps.id = accounts.sales_rep_id
ORDER BY accounts.name;

SELECT r.name region, a.name account, o.total_amt_usd/(o.total+.01) unit_price
FROM orders o
JOIN accounts a
ON a.id = o.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id


#SECTION 19

#Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.
SELECT r.name region, s.name sales_rep, a.name account
FROM sales_reps s
JOIN region r
ON s.region_id = r.id
AND r.name = 'Midwest'
JOIN accounts a
ON a.sales_rep_id = s.id
ORDER BY account;

#Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a first name starting with S and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name. 
SELECT r.name region, s.name sales_rep, a.name account
FROM sales_reps s
JOIN region r
ON s.region_id = r.id
AND r.name = 'Midwest'
AND s.name LIKE 'S%'
JOIN accounts a
ON a.sales_rep_id = s.id
ORDER BY account;

#Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a last name starting with K and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.
SELECT r.name region, s.name sales_rep, a.name account
FROM sales_reps s
JOIN region r
ON s.region_id = r.id
AND r.name = 'Midwest'
AND s.name LIKE '% K%'
JOIN accounts a
ON a.sales_rep_id = s.id
ORDER BY account;

#Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100. Your final table should have 3 columns: region name, account name, and unit price. In order to avoid a division by zero error, adding .01 to the denominator here is helpful total_amt_usd/(total+0.01). 
SELECT r.name region, a.name account, o.total_amt_usd/(o.total+0.001) unit_price
FROM orders o
JOIN accounts a
ON o.account_id = a.id
AND o.standard_qty > 100
JOIN sales_reps s
ON a.sales_rep_id = s.id
JOIN region r
ON s.region_id = r.id;

#Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. Sort for the smallest unit price first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01). 
SELECT r.name region, a.name account, o.total_amt_usd/(o.total+0.001) unit_price
FROM orders o
JOIN accounts a
ON o.account_id = a.id
AND o.standard_qty > 100
AND o.poster_qty > 50
JOIN sales_reps s
ON a.sales_rep_id = s.id
JOIN region r
ON s.region_id = r.id
ORDER BY unit_price;

#Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. Sort for the largest unit price first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).
SELECT r.name region, a.name account, o.total_amt_usd/(o.total+0.001) unit_price
FROM orders o
JOIN accounts a
ON o.account_id = a.id
AND o.standard_qty > 100
AND o.poster_qty > 50
JOIN sales_reps s
ON a.sales_rep_id = s.id
JOIN region r
ON s.region_id = r.id
ORDER BY unit_price DESC;

#What are the different channels used by account id 1001. Your final table should have only 2 columns: account name and the and the different channels. You can try SELECT DISTINCT to narrow SELECT DISTINCT a.name, we.channel
SELECT DISTINCT a.name, we.channel
FROM web_events we
JOIN accounts a
ON we.account_id = a.id
WHERE we.account_id = 1001

#Find all the orders that occurred in 2015. Your final table should have 4 columns: occurred_at, account name, order total, and order total_amt_usd.
SELECT o.occurred_at, a.name, o.total, o.total_amt_usd
FROM orders o
JOIN accounts a
ON a.id = o.account_id
WHERE o.occurred_at BETWEEN '2015-01-01' AND '2015-12-31'
ORDER BY o.occurred_at;