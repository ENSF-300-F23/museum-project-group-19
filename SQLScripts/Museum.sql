
DROP DATABASE IF EXISTS Museum;
CREATE DATABASE Museum;
USE Museum;

CREATE TABLE ARTIST_INFO (
  Artist_Name VARCHAR(100) NOT NULL,
  Birth_Year INT,
  Death_Year INT,
  Country_of_Origin VARCHAR(30),
  Art_Epoch VARCHAR(30),
  Primary_Style VARCHAR(30),
  Artist_Description VARCHAR(100),
  PRIMARY KEY (Artist_Name)
);

CREATE TABLE EXHIBIT_DETAILS (
  Exhibit_ID INT NOT NULL,
  Exhibit_Name VARCHAR(100) NOT NULL,
  Start_Date DATE,
  End_Date DATE,
  PRIMARY KEY (Exhibit_ID)
);

CREATE TABLE ART_PIECES (
  Piece_ID INT NOT NULL,
  Exhibit_ID INT,
  Piece_Title VARCHAR(200),
  Artist_Name VARCHAR(30),
  Creation_Year INT,
  Piece_Description VARCHAR(100),
  Art_Type VARCHAR(30),
  Piece_Origin VARCHAR(30),
  Art_Era VARCHAR(30),
  PRIMARY KEY (Piece_ID),
  FOREIGN KEY (Exhibit_ID) REFERENCES EXHIBIT_DETAILS(Exhibit_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Artist_Name) REFERENCES ARTIST_INFO(Artist_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PAINTINGS (
  Piece_ID INT NOT NULL,
  Paint_Type VARCHAR(50),
  Created_On VARCHAR(30),
  Painting_Style VARCHAR(30),
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE SCULPTURES (
  Piece_ID INT NOT NULL,
  Material_Used VARCHAR(30),
  Height_CM INT,
  Weight_KG FLOAT,
  Sculpture_Style VARCHAR(30),
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE OTHER_ART (
  Piece_ID INT NOT NULL,
  Art_Type VARCHAR(30),
  Art_Style VARCHAR(30),
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PERMANENT_COLLECTIONS (
  Piece_ID INT NOT NULL,
  Acquisition_Year INT,
  Collection_Status VARCHAR(30),
  Purchase_Cost INT,
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE GALLERY_COLLECTIONS (
  Collection_Name VARCHAR(200) NOT NULL,
  Collection_Type VARCHAR(30),
  Collection_Description VARCHAR(100),
  Collection_Address VARCHAR(150),
  Contact_Phone VARCHAR(30),
  Collection_Contact VARCHAR(30),
  PRIMARY KEY (Collection_Name)
);

CREATE TABLE BORROWED_ART (
  Collection_Name VARCHAR(200) NOT NULL,
  Piece_ID INT NOT NULL,
  Borrow_Date INT,
  Return_Date INT,
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Collection_Name) REFERENCES GALLERY_COLLECTIONS(Collection_Name) ON DELETE CASCADE ON UPDATE CASCADE
);