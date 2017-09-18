#Solution 1
SELECT id, account_id, occurred_at
FROM orders

#Solution 2
SELECT occurred_at, account_id, channel
FROM web_events
LIMIT 15

#Solution 3
SELECT id, occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at
LIMIT 10

SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC 
LIMIT 5

SELECT id, account_id, total
FROM orders
ORDER BY total
LIMIT 20

#Solution 4
SELECT occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at, total_amt_usd DESC
LIMIT 5

SELECT occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at DESC, total_amt_usd
LIMIT 10

#Solution 5
SELECT *
FROM orders
WHERE gloss_amt_usd >= 1000
LIMIT 5

SELECT *
FROM orders
WHERE total_amt_usd < 500
LIMIT 10

#Solution 6
SELECT name, website, primary_poc
FROM accounts
WHERE name = 'Exxon Mobil'

#Solution 7
SELECT
	id,
	account_id,
    standard_amt_usd / standard_qty
FROM orders
LIMIT 10

#Solution 8
SELECT id, account_id, standard_amt_usd/standard_qty AS unit_price
FROM orders

SELECT
	id,
	account_id,
    poster_amt_usd / (poster_amt_usd + gloss_amt_usd + standard_amt_usd) as poster_percent
FROM orders

#Solution 9
SELECT *
FROM accounts
WHERE name LIKE 'C%'

SELECT *
FROM accounts
WHERE name LIKE '%one%'

SELECT *
FROM accounts
WHERE name LIKE '%s'

#Solution 10
SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name IN ('Walmart', 'Target', 'Nordstrom')

SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords')

#Solution 11
SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name NOT IN('Walmart', 'Target', 'Nordstrom')

SELECT *
FROM web_events
WHERE channel NOT IN('organic', 'adwords')

SELECT *
FROM accounts
WHERE name NOT LIKE '%C'

SELECT *
FROM accounts
WHERE name NOT LIKE '%one%'

SELECT *
FROM accounts
WHERE name NOT LIKE 's%'

#Solution 12
SELECT *
FROM orders
WHERE standard_qty > 1000 AND poster_qty > 0 AND gloss_qty = 0

SELECT *
FROM accounts
WHERE name NOT LIKE 'C%' AND name LIKE '%s'

SELECT *
FROM web_events
#WHERE channel IN ('organic', 'adwords') AND occurred_at >= '2016-01-01' AND occurred_at <= '2016-12-31'
WHERE channel IN ('organic', 'adwords') AND occurred_at BETWEEN '2016-01-01' AND '2016-12-31'
ORDER BY occurred_at DESC

#Solution 13
SELECT id
FROM orders
WHERE gloss_qty > 4000 OR poster_qty > 4000

SELECT *
FROM orders
WHERE standard_qty = 0 AND (gloss_qty > 1000 OR poster_qty > 1000)

SELECT *
FROM accounts
WHERE (name LIKE 'C%' OR name LIKE 'W%')
AND (primary_poc LIKE '%ana%' OR primary_poc LIKE '%Ana%')
AND primary_poc NOT LIKE '%eana%'