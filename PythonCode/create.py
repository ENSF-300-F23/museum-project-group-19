# create.py
# 'group-19'
# Created by Qasim Amar, Said Rehmani, Siddhartha Paudel

import mysql.connector

cnx = mysql.connector.connect(
   host="127.0.0.1",
   port=3306,
   user='root',
   password= 'Password123!')

cur = cnx.cursor()

fd = open('SQLScripts/Museum.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')
for command in sqlCommands:
   try:
       if command.strip() != '':
           cur.execute(command)
   except (IOError):
       print("Command Skipped: ")