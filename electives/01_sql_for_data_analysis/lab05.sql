$ sqlite3 SoundMusicRecords.db

CREATE TABLE Album (
   ...> AlbumID INTEGER PRIMARY KEY,
   ...> Title TEXT,
   ...> ArtistID INTEGER,
   ...> FOREIGN KEY (ArtistID) REFERENCES ARTIST(ArtistID)
   ...> );
   
   
CREATE TABLE InvoiceLine (
    InvoiceLineID INTEGER PRIMARYKEY,
    InvoiceID INTEGER,
    TrackID INTEGER,
    UnitPrice REAL,
    Quantity INTEGER,
    FOREIGN KEY (InvoiceID) REFERENCES Invoice (InvoiceID),
    FOREIGN KEY (TrackID) REFERENCES Track (TrackID)
    );

#How many Pop songs have an "MPEG audio file" type?
sqlite> SELECT * FROM Genre;
sqlite> SELECT * FROM MediaType;

SELECT GenreID, COUNT(*) as Total
FROM Track JOIN MediaType
        ON (Track.MediaTypeID = MediaType.MediaTypeID)
WHERE (GenreID = '9' AND Track.MediaTypeID = '1');

#How many unique customers have purchased a Jazz track
sqlite> SELECT * FROM Genre;

SELECT COUNT(DISTINCT CustomerId)
FROM Invoice JOIN InvoiceLine, Track
    ON (Invoice.InvoiceId = InvoiceLine.InvoiceId
    AND InvoiceLine.TrackId = Track.TrackId)
WHERE Track.GenreId = '2';
    
#Which genre has the most songs of below average song length?
SELECT avg(Milliseconds) as AvgSongDuration FROM Track;

SELECT COUNT(Track.GenreID) as Genres, Genre.Name, AvgSongDuration
FROM (
    SELECT avg(Milliseconds) as AvgSongDuration FROM Track
    ) as durations, Track JOIN Genre ON (Track.GenreId = Genre.GenreId)
WHERE Milliseconds < AvgSongDuration
GROUP BY Track.GenreId
ORDER BY Genres
