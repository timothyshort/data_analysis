#Which 10 composers wrote the most songs in our dataset?
SELECT Composer, COUNT(*)
FROM Track
GROUP BY Composer
ORDER BY COUNT(*)
DESC
LIMIT 10;

#Which tracks in the dataset are between 2,500,000 and 2,600,000 milliseconds long?
#Return the name and the ms ordered by ms
SELECT Name, Milliseconds
FROM Track
WHERE Milliseconds > 2500000
AND Milliseconds < 2600000
ORDER BY Milliseconds;

#List albums written by either Iron Maiden or Amy Winhouse
#Return the Artist name followed by Album title
SELECT Artist.Name and Album.Title
FROM Artist, Album
WHERE Artist.ArtistId = Album.ArtistId
AND (Artist.ArtistId = 'Iron Maiden' OR Artist.ArtistId = 'Amy Winehouse');

SELECT Artist.Name, Album.Title
FROM Album JOIN Artist
ON Artist.ArtistId = Album.ArtistId
WHERE Name = 'Iron Maiden'
OR Name = 'Amy Winehouse';

#LAB

##  Write a query that returns the 3 countries with the highest number of invoices, along with the number ##  of invoices for these countries.
SELECT BillingCountry, Count (*) as Invoices
FROM Invoice
GROUP BY BillingCountry
ORDER BY Invoices DESC
LIMIT 3

##  Build a query that returns the person who has the highest sum of all invoices, along with their email, first name, and last name.
SELECT Email, FirstName, LastName, sum(Total) as Total
FROM Customer JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY Total DESC
LIMIT 1

##  Use your query to return the email, first name, last name, and Genre of all Rock Music listeners!
##  Return you list ordered alphabetically by email address starting with A.
##  Can you find a way to deal with duplicate email addresses so no one receives multiple emails?
SELECT Email, FirstName, LastName, Genre.Name as Genre
FROM Customer JOIN Invoice, InvoiceLine, Track, Genre
ON (Customer.CustomerId = Invoice.CustomerId
    AND Invoice.InvoiceId = InvoiceLine.InvoiceId
    AND InvoiceLine.TrackId = Track.TrackId
    AND Track.GenreId = Genre.GenreId)
WHERE Genre = "Rock"
GROUP BY Email
ORDER BY Email ASC

##  Write a query that returns the 1 city that has the highest sum of invoice totals.
##  Return both the city name and the sum of all invoice totals.
SELECT BillingCity, sum(Total) as Total
FROM Invoice
GROUP BY BillingCity
ORDER BY Total DESC
LIMIT 1

##  Return the top 3 most popular music genres for the city Prague with the highest invoice total
SELECT BillingCity, COUNT(*) as NumOfInvoices, Genre.Name as Genre
FROM Invoice JOIN InvoiceLine, Track, Genre
ON (Invoice.InvoiceId = InvoiceLine.InvoiceId
    AND InvoiceLine.TrackId = Track.TrackId
    AND Track.GenreId = Genre.GenreId)
WHERE BillingCity = 'Prague'
GROUP BY Genre
ORDER BY NumOfInvoices DESC
LIMIT 3;

##  Let's invite the artists who have written the most rock music in our dataset.
##  Write a query that returns the Artist name and total track count of the top 10 rock bands. 
SELECT Artist.Name, COUNT(*) as NumOfTracks
FROM Genre JOIN Track, Album, Artist
ON (Genre.GenreId = Track.GenreID
    AND Track.AlbumId = Album.AlbumId
    AND Album.ArtistId = Artist.ArtistId)
WHERE Genre.Name = "Rock"
GROUP BY Artist.Name
ORDER BY NumOfTracks DESC
LIMIT 10

##  Return the BillingCities in France, followed by the total number of  tracks purchased for Alternative & Punk music.
##  Order your output so that the city with the highest total number of tracks purchased is on top.
SELECT BillingCity, COUNT(*) as NumOfTracks
FROM Invoice JOIN InvoiceLine, Track, Genre
ON (Invoice.InvoiceId = InvoiceLine.InvoiceId
    AND InvoiceLine.TrackId = Track.TrackId
    AND Track.GenreId = Genre.GenreId)
WHERE Genre.Name = 'Alternative & Punk'
    AND BillingCountry = 'France'
GROUP BY BillingCity
ORDER BY NumOfTracks DESC