#3

#In the accounts table, there is a column holding the website for each company. The last three digits specify what type of web address they are using. A list of extensions (and pricing) is provided here. Pull these extensions and provide how many of each website type exist in the accounts table.
SELECT DISTINCT RIGHT(website,3) as extension
FROM accounts

SELECT RIGHT(website,3) as extensions, count(*) as count
FROM accounts
GROUP BY RIGHT(website,3)

#There is much debate about how much the name (or even the first letter of a company name matters). Use the accounts table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number). 
SELECT LEFT(name, 1) as letter, count(*) as count
FROM accounts
GROUP BY LEFT(name, 1)
ORDER BY count DESC

#Use the accounts table and a CASE statement to create two groups: one group of company names that start with a number and a second group of those company names that start with a letter. What proportion of company names start with a letter?
SELECT sum(number) as numbers, sum(letter) as letters
FROM
(SELECT name,
	CASE WHEN LEFT(name, 1) IN ('0','1','2','3','4','5','6','7','8','9') THEN 1 ELSE 0
    END as number,
	CASE WHEN LEFT(name, 1) IN ('0','1','2','3','4','5','6','7','8','9') THEN 0 ELSE 1
    END as letter
FROM accounts) t1

#Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, and what percent start with anything else?
SELECT sum(vowels) as numbers, sum(consonants) as letters
FROM
(SELECT name,
	CASE WHEN LEFT(name, 1) IN ('A','E','I','O','U') THEN 1 ELSE 0
    END AS vowels,
	CASE WHEN LEFT(name, 1) IN ('A','E','I','O','U') THEN 0 ELSE 1
    END AS consonants
FROM accounts) t1


#6

#Use the accounts table to create a first and last name column that hold the first and last names for the primary_poc. 
SELECT primary_poc,
	POSITION(' ' IN primary_poc) AS whitespace,
    LEFT(primary_poc, POSITION(' ' IN primary_poc) -1) AS first_name,
    RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) AS last_name
FROM accounts

#Now see if you can do the same thing for all of the name of each rep in the sales_rep table. Again provide a first and last name column.
SELECT name,
    LEFT(name, POSITION(' ' IN name) -1) AS first_name,
    RIGHT(name, LENGTH(name) - POSITION(' ' IN name)) AS last_name
FROM sales_reps


#9

#Each company in the accounts table wants to create an email address for each primary_poc. The email address should be the first name of the primary_poc . last name primary_poc @ company name .com.
SELECT CONCAT(
  LEFT(primary_poc, POSITION(' ' IN primary_poc) -1),
  '.',
  RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)),
  '@',
  name,
  '.com')
  as email
FROM accounts