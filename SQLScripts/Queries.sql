--@block
-- Museum Query
-- 'group-19'
-- Created by Qasim Amar, Said Rehmani, Siddhartha Paudel

USE MUSEUM;

--@block
-- A basic retrieval query; Retrieves the name of the exhibitions presented in the database with the start and end date
SELECT Exhibit_Name, Start_Date, End_Date FROM EXHIBIT_DETAILS;

--@block
-- A retrieval query with ordered results; Retrieves the name and year born from artist_info born before 1650 and orderd from youngest to oldest.
SELECT Artist_Name, Birth_Year FROM ARTIST_INFO
WHERE Birth_Year < 1650 AND Birth_Year IS NOT NULL
ORDER BY Birth_Year ASC;

--@block
-- A nested retrieval query; Retrieves the title, author and year made for paintings created on wood
SELECT Piece_Title, Artist_Name, Creation_Year FROM ART_PIECES
WHERE ID_NO IN (SELECT ID_NO FROM PAINTINGS WHERE Created_On = 'Wood');

--@block
-- A retrieval query using joined tables; Retrieves the art pieces which are borrowed in the museum
SELECT Piece_Title, Creation_Year FROM ART_PIECES
JOIN BORROWED_ART ON ART_PIECES.ID_NO = BORROWED_ART.Piece_ID;