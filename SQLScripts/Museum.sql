-- Museum Database SQL Script
-- 'group-19'
-- Created by Qasim Amar, Said Rehmani, Siddhartha Paudel

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
  ID_NO INT NOT NULL,
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
  ID_NO INT NOT NULL,
  Paint_Type VARCHAR(50),
  Created_On VARCHAR(30),
  Painting_Style VARCHAR(30),
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE SCULPTURES (
  ID_NO INT NOT NULL,
  Material_Used VARCHAR(30),
  Height_CM INT,
  Weight_KG FLOAT,
  Sculpture_Style VARCHAR(30),
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE OTHER_ART (
  ID_NO INT NOT NULL,
  Art_Type VARCHAR(30),
  Art_Style VARCHAR(30),
  FOREIGN KEY (Piece_ID) REFERENCES ART_PIECES(Piece_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PERMANENT_COLLECTIONS (
  ID_NO INT NOT NULL,
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


FOREIGN KEY (ID_NO) REFERENCES ART_OBJECTS(ID_NO) WITH DELETE CASCADE AND UPDATE CASCADE,
FOREIGN KEY (COLLECTIONS) REFERENCES COLLECTIONS(NAME) WITH DELETE CASCADE AND UPDATE CASCADE


INSERT INTO ARTIST
VALUES      ('Marcus Gheeraerts the Younger', 1561, 1636, 'Belgium', 'Baroque', "Portraits", "Painter"),
            ('Hans Holbein the Younger', 1498, 1543, 'United Kingdom', 'Renaissance', "Portraits", "Painter"),
            ('Pietro Torrigiano', 1472, 1528, 'Italy', 'Renaissance', "Sculptures", "Sculpter"),
            ('Jacob Halder', 1558, 1608, 'United Kingdom', 'Elizabethan Era', "Sculptures", "Sculpter"),
            ('Cornelius Norbertus Gijsbrechts', 1630, 1683, 'Belgium', 'Reformation and Enlightenment', "Abtract", "Painter"),
            ('Georges Braque', 1882, 1963, 'France', 'Industrial', "Impressionist", "Painter"),
            ('Juan Gris', 1887, 1927, 'Spain', 'Industrial', "Abstract", "Painter"),
            ('William Michael Harnett', 1848, 1892, 'Ireland', 'Common Era', "Realism", "Painter"),
            ('Simone Leigh', 1967, null, 'United States', 'Modern Era', "Sculptures", "Sculpter"),
            ('David Drake', 1800, 1865, 'United States', 'Industrial Revolution', "Sculptures", "Sculptor"),
            ('Leonardo da Vinci', 1452, 1519, 'Italy', 'Renaissance', "Science and Humans", "Painter/Sculptor/Scientist"),
            ('Jean-Honoré Fragonard', 1732, 1806, 'France', 'Reformation and Enlightenment', "Portraits/Scenes", "Painter"),
            ('Alexandros of Antioch', null, null, 'Greece', 'Ancient', "Sculptures", "Sculptor"),
            ('François Gérard', 1770, 1837, 'Italy', 'Reformation and Enlightenment', "Portraits", "Painter"),
            ('Elias van Nijmegen', 1667, 1755, 'Netherlands', 'Early Modern Era', "Abstract", "Painter");
            ('Augustin Quesnel', 1595, 1661, 'France', 'Fronde', "Portraits", "Painter");


INSERT INTO EXHIBITIONS
VALUES      (200000, 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
            (200001, "Cubism and the Trompe l'Oeil Tradition", '2022-10-20', '2023-01-22'),
            (200002, 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05'),
            (200003, "The Master Pieces of the Louvre", '2022-12-10', '2023-01-10');

INSERT INTO ART_OBJECTS
VALUES      (100001, 200000,'Ellen Maurice','Marcus Gheeraerts the Younger',1597,'Upper Body Portrait','Painting','Flemish','Elizabethan Era'),
            (100002, 200000,'Hermann von Wedigh III','Hans Holbein the Younger',1532,'Upper Body Portrait','Painting','German','Renaissance'),
            (100003, 200000,'Portrait Bust of John Fisher, Bishop of Rochester','Pietro Torrigiano',1515,'Human Sculpture','Sculpture','Italian','Renaissance'),
            (100004, 200000,'Armor Garniture of George Clifford ','Jacob Halder',1608,'Body Armour','Sculpture','British','Elizabethan Era'),
            (100005, 200000,'Tazza',null,1599,'Wine Cup','Other','British','Elizabethan Era'),
            (100006, 200000,'Blackwork Embroidery',null,1590,'Silk Embroidery','Other','British','Elizabethan Era'),

            (100007, 200001,'The Attributes of the Painter','Cornelius Norbertus Gijsbrechts',1665,'Abstract','Painting','Flemish','Spanish Baroque'),
            (100008, 200001,'Violin and Sheet Music: "Petit Oiseau"','Georges Braque',1913,'Impressionist','Painting','French','Industrial'),
            (100009, 200001,'Violin and Engraving','Juan Gris',1913,'Abtract','Painting','Spanish','Industrial'),
            (100010, 200001,'Still Life—Violin and Music','William Michael Harnett',1888,'Abstract','Painting','Spanish','Common Era'),

            (100011, 200002,'Face Jug Series', 'Simone Leigh', 2019,'Sculpture','Jug with face ','American','Modern era'),
            (100012, 200002,'Storage Jar', 'David Drake', 1858, 'Stores Items as a big pot', 'Sculpture', 'American', 'Industrial Revolution'),
            (100013, 200002,'Power figure',null,1850,'Metal sculpture depicting human','Sculpture',null,'Industrial Revolution'),
            (100014, 200002,'Tiki Representing the Deity Rongo', null, 1808,'Male Tiki','Sculpture','Mangareva','Pre-European Contact'),

            (100015, 200003,'Monna Lisa','Leonardo da Vinci',1519,'Portrait','Painting','Italian','Renaissance'),
            (100016, 200003,'Bacchante endormie','Jean-Honoré Fragonard',1765,'Portrait','Painting','French','Ancien Régime'),
            (100017, 200003,'Venus of Milo','Alexandros of Antioch',-150,'Human Sculpture','Sculpture','Greek','Hellenistic'),
            (100018, 200003,"L'impératrice Marie-Louise",'François Gérard',1810,'Portrait','Painting','French','Napoleonic era'),
            (100019, 200003,"Panneau décoratif avec guirlande de fleurs tombant d'un vase et tenue par deux amours",'Elias van Nijmegen',1716,'Abstract','Painting','French','Early Modern Era'),
            (100020, 200003,"Portrait d'homme",'Augustin Quesnel',1652,'Upper body portrait','Painting','French','Fronde');



INSERT INTO PAINTING
VALUES      (100001, 'Oil', 'Wood', 'Portrait'),
            (100002, 'Oil and Gold', 'Wood', 'Portrait'),
            (100007, 'Oil', 'Canvas', 'Abstract'),
            (100008, 'Oil and Charcoal', 'Canvas', 'Impressionist'),
            (100009, 'Oil, Sand and Collage', 'Canvas', 'Abstract'),
            (100010, 'Oil', 'Canvas', 'Abstract'),
            (100015, 'Oil', 'Wood', 'Portrait'),
            (100016, 'Oil', 'Canvas', 'Portrait'),
            (100018, 'Oil', 'Canvas', 'Scenic Depiction'),
            (100019, 'Oil', 'Canvas', 'Scenic Depiction'),
            (100020, 'Oil', 'Wood', 'Portrait');
            

INSERT INTO SCULPTURE
VALUES      (100003, 'Polychrome Terracotta', 61.6, 65.7, 'Human'),
            (100004, 'Steel, Gold, Leather, and Textile', 176.5, 10, 'Historical'),
            (100011, 'Salt-fired porcelain', 44.5, 29.5, 'Jug'),
            (100012, 'Alkaline-glazed stoneware', 64, 30, 'Pot'),
            (100013, 'Wood, iron, nails, blades and fragments, and fiber cord', 40.75, 13.75, 'Statue'),
            (100014, 'Wood', 60.75, 33.75, 'Statue'),
            (100017, 'Marble', 154, null, 'Human');


            
INSERT INTO OTHER
VALUES      (100005, 'Tool', 'Luxurious'),
            (100006, 'Textile', 'Luxurious');


INSERT INTO PERMANENT
VALUES      (100001, 2022, "Owned", 192384),
            (100002, 2022, "Owned", 493058),
            (100003, 2022, "Owned", 49024),
            (100004, 2022, "Owned", 93284),
            (100005, 2022, "Owned", 94823),
            (100006, 2022, "Owned", 42000),
            (100007, 2022, "Owned", 90234),
            (100008, 2022, "Owned", 12822),
            (100009, 2022, "Owned", 13421),
            (100010, 2022, "Owned", 789987),
            (100011, 2022, "Owned", 13101),
            (100012, 2022, "Owned", 18920),
            (100013, 2022, "Owned", 9204),
            (100014, 2022, "Owned", 24244);
            

INSERT INTO COLLECTIONS
VALUES      ('Departement des Peintures', 'Paintings', 'Historical Paintings', "Louvre Museum, Rue de Rivoli, 75001 Paris, France", "+33 1 40 20 50 50", "Laurence des Cars"),
            ('Département des Antiquités orientales', 'Sculptures', 'Historical sculptures and tools', "Louvre Museum, Rue de Rivoli, 75001 Paris, France", "+33 1 40 20 50 50", "Laurence des Cars"),
            ('Département des Sculptures du Moyen Age, de la Renaissance et des temps modernes', 'Sculptures', 'Historical sculptures and tools', "Louvre Museum, Rue de Rivoli, 75001 Paris, France", "+33 1 40 20 50 50", "Laurence des Cars");
            

INSERT INTO BORROWED
VALUES      ('Departement des Peintures', 100015, 2022, null),
            ('Departement des Peintures', 100016, 2022, null),
            ('Département des Antiquités orientales', 100017, 2022, null),
            ('Département des Sculptures du Moyen Age, de la Renaissance et des temps modernes', 100018, 2022, null),
            ('Departement des Peintures', 100019, 2022, null),
            ("Département des Antiquités orientales", 100020, 2022, null);