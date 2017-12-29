#Labs
select * from invoice;

SELECT max(Total) FROM Invoice WHERE BillingCountry="Spain";

SELECT title FROM Employee WHERE LastName = "Johnson";

.schema Invoice;

#Exercise: find the composer who has the minimum average length song
.schema Track
SELECT Composer, Milliseconds FROM Track;
SELECT Composer, Name, avg(Milliseconds) FROM Track GROUP BY Composer;
SELECT Composer, Name, avg(Milliseconds) FROM Track GROUP BY Composer ORDER BY avg(Milliseconds);
SELECT Composer, Name, avg(Milliseconds) FROM Track GROUP BY Composer ORDER BY (Milliseconds) DESC;
SELECT Composer, Name, avg(Milliseconds) FROM Track GROUP BY Composer ORDER BY avg(Milliseconds) LIMIT 1;